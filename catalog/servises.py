from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories():
    if CACHE_ENABLED:
        key = f'categories_list'
        categories = cache.get(key)

        if not categories:
            # Если данные не найдены в кеше, выполняем запрос к базе данных
            categories = Category.objects.all()
            # Кешируем результат на 1 час
            cache.set('categories_list', categories, 3600)
    else:
        categories = Category.objects.all()

    return categories