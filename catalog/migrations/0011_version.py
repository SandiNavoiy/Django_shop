# Generated by Django 4.2.2 on 2023-07-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_version', models.FloatField(default=1.0, verbose_name='номер версии')),
                ('name_of_version', models.CharField(max_length=100, verbose_name='имя версии')),
                ('is_activ', models.BooleanField(default=True, verbose_name='статус актуальности')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='название продукта')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
