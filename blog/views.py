from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView

from blog.models import BlogPost


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost

class BlogPostDetailView(DetailView):
    model = BlogPost

class BlogPostCreateView(CreateView):
    model = BlogPost

class BlogPostUpdateView(UpdateView):
    model = BlogPost

class BlogPostDeleteView(DeleteView):
    model = BlogPost