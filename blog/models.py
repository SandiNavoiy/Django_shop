from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    preview_image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'запись'  # Настройка для наименования одного объекта
        verbose_name_plural = 'записи'  # Настройка для наименования набора объектов