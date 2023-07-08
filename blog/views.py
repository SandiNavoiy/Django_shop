from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView

from blog.forms import BlogPostForm
from blog.models import BlogPost


# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_post_create.html'
    success_url = 'http://127.0.0.1:8000/'  # редирект



class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail('Просмотры', 'Количество просмотров 100')
        return self.object

class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'

    def get(self, request, slug):
        blog = get_object_or_404(self.model, slug=slug)
        return render(request, 'blog/blog_post_update.html', {'blog': blog})

    def post(self, request, slug):
        blog = get_object_or_404(self.model, slug=slug)
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Остальные поля...

        blog.title = title
        blog.content = content
        # Обновить остальные поля...
        blog.save()
        return redirect('blog/blog_post_detail', slug=blog.slug)


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('blog:blog_post_list')