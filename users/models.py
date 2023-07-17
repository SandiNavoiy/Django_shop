import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='страна')
    reset_password_token = models.CharField(max_length=100, blank=True, null=True)

    # переопределение поля user  как основного для идентификации на емаил
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
