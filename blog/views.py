from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView

from blog.forms import BlogPostForm
from blog.models import BlogPost
from config import settings


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
    success_url = 'http://127.0.0.1:8000/blog/list/'  # редирект


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

    success_url = 'http://127.0.0.1:8000/blog/list/'


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('blog:blog_post_list')
