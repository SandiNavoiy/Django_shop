from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='наименование')
    description_product = models.TextField(verbose_name='описание')
    picture_product = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='изображение')
    category_name = models.ForeignKey(max_length=150, verbose_name='категория')
    price_product = models.IntegerField(max_length=150, verbose_name='цена за покупку')
    date_of_creation_product = models.DateTimeField(max_length=150, verbose_name='дата создания')
    last_modified_date_product = models.DateTimeField(max_length=150, verbose_name='дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.description_product} ' \
               f'{self.category_name} {self.price_product} {self.date_of_creation_product} {self.last_modified_date_product}'

    class Meta:
        verbose_name = 'продукт' # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты' # Настройка для наименования набора объектов

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='название')
    description_category = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name} {self.description_category}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов