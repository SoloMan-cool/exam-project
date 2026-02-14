from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True, verbose_name='Фото пользователя')
    email = models.EmailField(unique=True)

