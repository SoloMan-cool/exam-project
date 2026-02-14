from django.db import models
from apps.common.models import BaseTimedModel


class Shop(BaseTimedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

class Category(BaseTimedModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(verbose_name='Короткая ссылка')
    icon = models.ImageField(upload_to='categories/icons/', null=True, blank=True, verbose_name='Иконка')

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'