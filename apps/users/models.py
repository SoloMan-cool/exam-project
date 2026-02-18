from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.models import BaseTimedModel


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True, verbose_name='Фото пользователя')

class Wishlist(BaseTimedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Избранное')


class WishlistItem(BaseTimedModel):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='wishlist_items')