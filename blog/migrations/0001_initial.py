# Generated by Django 4.2.2 on 2023-07-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('preview_image', models.ImageField(upload_to='blog_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
