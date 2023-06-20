from django.contrib import admin

from catalog.models import Category, Product

# Register your models here.
#admin.site.register(Category)  #регистрация модели
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('description_category', 'category_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category_name', 'price_product')
    list_filter = ('category_name',)
    search_fields = ('product_name', 'description_product',)
