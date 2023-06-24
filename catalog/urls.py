from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, categorii, products

urlpatterns = [
    path('', index),  # вывод главной страницы
    path('contacts', contacts, name='contact'),
    path('categorii', categorii, name='categorii'),
    path('products/<int:pk>/', products, name='product')# вывод страницы контактов

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Это добавляется один раз на проект