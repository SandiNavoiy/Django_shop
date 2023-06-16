from django.shortcuts import render

def index(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    if request.method == 'POST':
        print(f"Имя: {request.POST.get('name')}")
        print(f"Электронная почта: {request.POST.get('email')}")
        print(f"Текст сообщения: {request.POST.get('text')}")

    return render(request, 'catalog/contacts.html')
