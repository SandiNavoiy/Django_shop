from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogDeleteView, BlogCreateView, BlogUpdateView

app_name = BlogConfig.name
urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog_post_list'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('delete/<slug:slug>/', never_cache(BlogDeleteView.as_view()), name='delete'),
    path('create', never_cache(BlogCreateView.as_view()), name='create'),
    path('update/<slug:slug>/', never_cache(BlogUpdateView.as_view()), name='update'),

]
