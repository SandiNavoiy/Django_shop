from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView

from catalog.forms import ProductForm, CategoryForm, VersionForm
from catalog.models import Product, Category, Version


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        # get_queryset - запрос на выборку данных из БД
        queryset = super().get_queryset()
        # фильтр всех активные версии (active_versions), находим
        # только те версии, содержащие текущий продукт (product).
        # поле product_name для замены версии с продуктом
        # first(), чтобы получить первую найденную активную версию.
        active_versions = Version.objects.filter(is_activ=True)
        for product in queryset:
            product.active_version = active_versions.filter(product_name=product).first()
        return queryset


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

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context['formset'] = ProductFormset(self.request.POST)
        else:
            context['formset'] = ProductFormset()

        return context

    def form_valid(self, form):

        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/create_categor.html'

    success_url = reverse_lazy('catalog:categorii')  # редирект


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/delete_form.html'
    success_url = reverse_lazy('catalog:index')


class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/update_form.html'

    def get_success_url(self) -> str:
        new_url = slugify(self.object.pk)
        return reverse('catalog:product', args=[new_url])

    def get_context_data(self, **kwargs):
        # обработка post и get запросов
        context_data = super().get_context_data()
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
