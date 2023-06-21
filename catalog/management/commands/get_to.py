import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очистка старых данных
        Product.objects.all().delete()
        # Загрузка данных из файла JSON
        with open('Product_data.json ') as file:
            data = json.load(file)
        products = []
        for item in data:
            category_name = item['fields']['category_name']
            category = Category.objects.get(pk = category_name)
            product = Product(
                    product_name = item['fields']['product_name'],
                    description_product = item['fields']['description_product'],
                    picture_product = item['fields']['picture_product'],
                    category_name = category,
                    price_product = item['fields']['price_product'],
                    date_of_creation_product = item['fields']['date_of_creation_product'],
                    last_modified_date_product = item['fields']['last_modified_date_product']

                )
            products.append(product)



        Product.objects.bulk_create(products)

