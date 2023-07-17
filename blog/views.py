from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView

from blog.forms import BlogPostForm
from blog.models import BlogPost
from catalog.forms import ProductForm, CategoryForm, VersionForm
from catalog.models import Product, Category, Version


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
    success_url = reverse_lazy('blog:blog_post_list')  # редирект


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 10:
            send_mail('Просмотры', 'Количество просмотров 100', settings.EMAIL_HOST_USER, ['kochetov11@yandex.ru'])
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_post_form.html'

    def get_success_url(self) -> str:
        new_slug = slugify(self.object.title)
        return reverse('blog:detail', args=[new_slug])




class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('blog:blog_post_list')
