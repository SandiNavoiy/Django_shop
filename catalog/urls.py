from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoriiListView, ProductsDetailView, ProductsCreateView, UserDetailView, \
    IndexListView, CategoryCreateView

app_name = CatalogConfig.name
urlpatterns = [
                  path('', IndexListView.as_view(), name='index'),  # вывод главной страницы
                  path('contacts/', UserDetailView.as_view(), name='contact'),
                  path('categorii', CategoriiListView.as_view(), name='categorii'),
                  path('products/<int:pk>/', ProductsDetailView.as_view(), name='product'),
                  path('create', ProductsCreateView.as_view(), name='create_product'),
                  path('create_cat', CategoryCreateView.as_view(), name='create_cat')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Это добавляется один раз на проект
