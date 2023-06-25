from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.shortcuts import render, redirect



from catalog.models import Product, Contact, Category


def index(request):
    latest_products = Product.objects.order_by('-id')[:5]
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_products = paginator.get_page(page_number)
    context = {
        'products': page_products
    }
    #5 послнедних с конца
    for product in latest_products:
        print(product.product_name)  # Вывод товаров в консоль
    return render(request, 'catalog/index.html', context)


def contacts(request):
    user = User.objects.get(id=1)  # Здесь 1 - ID пользователя, которого вы хотите отобразить, для примера админа
    #Словарь который мы передаем в шаблон, с ключем user
    # В шаблоне используем шаблонные переменные {{ user.username }}и {{ user.email }}для представления данных пользователя
    # хотя странно почему именно user.username а не context.username?
    context = {
        'user': user,
    }
    if request.method == 'POST':
        print(f"Имя: {request.POST.get('name')}")
        print(f"Электронная почта: {request.POST.get('email')}")
        print(f"Текст сообщения: {request.POST.get('message')}")

    return render(request, 'catalog/contacts.html', context)


def products(request, pk):
    item = Product.objects.get(pk=pk)

    context = {
        'item': item

    }
    return render(request, 'catalog/products.html', context=context)


def categorii(request):
    сategor = Category.objects.all()

    context = {
        'сategory': сategor
    }


    return render(request, 'catalog/categorii.html', context)


