from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView

app_name = BlogConfig.name
urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog_post_list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='blog_post_detail'),
]