import json

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очистка старых данных
        Product.objects.all().delete()
        # Загрузка данных из файла JSON
        with open('Product_data.json ') as file:
            data = json.load(file)
        products = []
        for item


        Product.objects.bulk_create(products)


            product_name = models.CharField(max_length=100, verbose_name='наименование')
            description_product = models.TextField(verbose_name='описание')
            picture_product = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='изображение')
            category_name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
            price_product = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='цена за покупку')
            date_of_creation_product = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
            last_modified_date_product = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')