from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView

from blog.models import BlogPost


# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_post_create.html'

    def get(self, request):
        # Отобразить форму создания блога
        return render(request, 'blog_create.html')

    def post(self, request):
        # Обработать отправку формы создания блога
        title = request.POST.get('title')
        content = request.POST.get('content')

        blog = self.model.objects.create(title=title, content=content)
        return redirect('blog_detail', slug=blog.slug)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'

    def get_object(self, queryset=None):
        get_item = super().get_object(queryset)
        get_item.views_count += 1
        get_item.save()
        print()
        return get_item



    # def get(self, request, slug):
    #     blog = get_object_or_404(self.model, slug=slug)
    #     blog.increase_views_count()  # Увеличить счетчик просмотров
    #     return render(request, 'blog/blog_post_detail.html', {'blog': blog})


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'

    def get(self, request, slug):
        blog = get_object_or_404(self.model, slug=slug)
        return render(request, 'blog_update.html', {'blog': blog})

    def post(self, request, slug):
        blog = get_object_or_404(self.model, slug=slug)
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Остальные поля...

        blog.title = title
        blog.content = content
        # Обновить остальные поля...
        blog.save()
        return redirect('blog_detail', slug=blog.slug)


class BlogDeleteView(DeleteView):
    model = BlogPost

    def post(self, request, slug):
        blog = get_object_or_404(self.model, slug=slug)
        blog.delete()
        return redirect('blog_list')