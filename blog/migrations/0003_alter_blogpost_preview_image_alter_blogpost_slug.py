# Generated by Django 4.2.2 on 2023-07-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_content_alter_blogpost_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/', verbose_name='медиа'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='слуг'),
        ),
    ]