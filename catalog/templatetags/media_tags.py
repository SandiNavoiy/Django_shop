from django import template
from django.conf import settings

register = template.Library()

#@register.image
#def mediapath(file_path):
#    media_url = settings.MEDIA_URL
#    return f"{media_url}{file_path}"
