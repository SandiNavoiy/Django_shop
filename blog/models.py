from django.db import models
from django.utils.text import slugify

NULLABLE = {'null': True, 'blank': True}

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, unique=True, verbose_name='слуг', **NULLABLE)
    content = models.TextField(verbose_name='текст')
    preview_image = models.ImageField(upload_to='blog_images/', verbose_name='медиа', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='статус публикации')
    views_count = models.IntegerField(default=0, verbose_name='счетчик просмотров')



    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'запись'  # Настройка для наименования одного объекта
        verbose_name_plural = 'записи'  # Настройка для наименования набора объектов