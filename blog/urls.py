from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogDeleteView

app_name = BlogConfig.name
urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog_post_list'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
 #   path('entry_update/<slug:slug>/', BlogEntryUpdateView.as_view(), name='entry_update'),
#    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='entry_delete'),

]