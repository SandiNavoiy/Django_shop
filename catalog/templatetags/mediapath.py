from django import template

from django.conf import settings


register = template.Library()

@register.filter
def mediapath(value):
    # Получаем путь к медиафайлам из настроек Django
    media_url = settings.MEDIA_URL

    # Объединяем путь к медиафайлу с базовым URL медиафайлов
    media_path = f"{media_url}{value}"

    return media_path