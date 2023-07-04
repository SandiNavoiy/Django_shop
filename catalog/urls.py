from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, create_product, CategoriiListView, ProductsDetailView

urlpatterns = [
    path('', index),  # вывод главной страницы
    path('contacts', contacts, name='contact'),
    path('categorii', CategoriiListView.as_view(), name='categorii'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='product'),
    path('create', create_product, name='create_product')# вывод страницы контактов

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Это добавляется один раз на проект
