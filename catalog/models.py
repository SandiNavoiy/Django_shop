from django.contrib.auth.models import User
from django.db import models



# Create your models here.
NULLABLE = {'null': True, 'blank': True}
class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='название')
    description_category = models.TextField(verbose_name='описание')
    picture_category = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='изображение')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name}'

    class Meta:
        # Метакласс описания
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('category_name',)  # настройка сортировки


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    description_product = models.TextField(verbose_name='описание')
    picture_product = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='изображение')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price_product = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='цена за покупку')
    date_of_creation_product = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date_product = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} '

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов




class Version(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='название продукта')
    number_of_version = models.FloatField(default=1.0, verbose_name="номер версии")
    name_of_version = models.CharField(max_length=100, verbose_name="имя версии")
    is_activ = models.BooleanField(default=True, verbose_name='статус актуальности')


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.number_of_version}  {self.name_of_version}'

    class Meta:
        verbose_name = 'версия'  # Настройка для наименования одного объекта
        verbose_name_plural = 'версии'  # Настройка для наименования набора объектов


