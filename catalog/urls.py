from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, categorii, products, create_product

urlpatterns = [
    path('', index),  # вывод главной страницы
    path('contacts', contacts, name='contact'),
    path('categorii', categorii, name='categorii'),
    path('products/<int:pk>/', products, name='product'),
    path('create', create_product, name='create_product')# вывод страницы контактов

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Это добавляется один раз на проект