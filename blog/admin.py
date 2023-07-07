from django.contrib import admin

from blog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
    # описание отображения в админке
    #list_display = ('title')
    # описание фильтра в админке
    #list_filter = ('title', 'is_published')
    # описание доступных полей поиска в админке
    #search_fields = ('title')