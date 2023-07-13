from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.
# admin.site.register(Category)  #регистрация модели
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('description_category', 'category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # описание отображения в админке
    list_display = ('id', 'product_name', 'category_name', 'price_product')
    # описание фильтра в админке
    list_filter = ('category_name',)
    # описание доступных полей поиска в админке
    search_fields = ('product_name', 'description_product',)
    
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'number_of_version', 'name_of_version', 'is_activ')
