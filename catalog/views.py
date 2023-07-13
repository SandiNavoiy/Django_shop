from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product, Category, Version


#def index(request):
#    products = Product.objects.all()
#    paginator = Paginator(products, 6)
#    page_number = request.GET.get('page')
#    page_products = paginator.get_page(page_number)
#    context = {
#        'products': page_products
#    }
#    # 5 послнедних с конца

    #return render(request, 'catalog/index.html', context)
class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        # фильтр всех активные версии (active_versions), находим
        # только те версии, содержащие текущий продукт (product).
        # поле product_name для замены версии с продуктом
        #first(), чтобы получить первую найденную активную версию.
        active_versions = Version.objects.filter(is_activ=True)
        for product in queryset:
            product.active_version = active_versions.filter(product_name=product).first()
        return queryset





#def contacts(request):
#    user = User.objects.get(id=1)  # Здесь 1 - ID пользователя, которого вы хотите отобразить, для примера админа
#    # Словарь который мы передаем в шаблон, с ключем user
    # В шаблоне используем шаблонные переменные {{ user.username }}и {{ user.email }}для представления данных пользователя
    # хотя странно почему именно user.username а не context.username?
#    context = {
#        'user': user,
#    }
#    if request.method == 'POST':
#        print(f"Имя: {request.POST.get('name')}")
#        print(f"Электронная почта: {request.POST.get('email')}")
#        print(f"Текст сообщения: {request.POST.get('message')}")

#    return render(request, 'catalog/contacts.html', context)
class UserDetailView(DetailView):
    model = User
    template_name = 'catalog/contacts.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        # Возвращаем первого пользователя
        return User.objects.first()

# def products(request, pk):
#    item = Product.objects.get(pk=pk)

#    context = {
#        'item': item

#    }
#    return render(request, 'catalog/products.html', context=context)
class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'item'
    pk_url_kwarg = 'pk'


# def categorii(request):
#    сategor = Category.objects.all()
#    context = {
#        'сategory': сategor
#    }
#    return render(request, 'catalog/categorii.html', context)

class CategoriiListView(ListView):
    model = Category
    template_name = 'catalog/categorii.html'
    context_object_name = 'сategory'


# def create_product(request):
#    if request.method == 'POST':
#        form = ProductForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('/#')
#    else:
#        form = ProductForm()

#    return render(request, 'catalog/create_product.html', {'form': form})


class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'

    success_url = reverse_lazy('catalog:index')  # редирект
