from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product, Contact, Category



class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    paginate_by = 6



class UserDetailView(DetailView):
    model = User
    template_name = 'catalog/contacts.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        # Возвращаем первого пользователя
        return User.objects.first()


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'item'
    pk_url_kwarg = 'pk'


class CategoriiListView(ListView):
    model = Category
    template_name = 'catalog/categorii.html'
    context_object_name = 'сategory'



class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'

    success_url = reverse_lazy('catalog:index')  # редирект
