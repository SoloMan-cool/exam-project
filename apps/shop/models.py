from django.db import models
from apps.common.models import BaseTimedModel
from apps.users.models import User

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

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tags(BaseTimedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

from decimal import Decimal

class Product(BaseTimedModel):
    class StatusChoices(models.TextChoices):
        sold = 'sold', 'Sold'
        new = 'new', 'New'
        sale = 'sale', 'Sale'

    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='Короткая ссылка')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Цена')
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        null=True,
        blank=True,
        verbose_name='Статус'
    )

    quantity = models.SmallIntegerField(default=7, verbose_name='Кол-во')
    sale_percent = models.SmallIntegerField(
        default=0,
        verbose_name='Процент скидки',
        help_text='данное поле заполняем если статус sale'
    )

    preview = models.ImageField(
        verbose_name='Заставка',
        upload_to='products/previews/'
    )

    categories = models.ManyToManyField(
        Category,
        related_name='products',
        verbose_name='категории',
        blank=True
    )

    tags = models.ManyToManyField(
        Tags,
        related_name='products',
        verbose_name='теги',
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.quantity <= 0:
            self.status = self.StatusChoices.sold
        super().save(*args, **kwargs)

    @property
    def discounted_price(self):
        if self.status == self.StatusChoices.sale and self.sale_percent > 0:
            discount = (self.price * Decimal(self.sale_percent)) / Decimal(100)
            return self.price - discount
        return self.price


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class ProductReview(BaseTimedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()

    def __str__(self):
        return f'{self.product.name} - {self.user.username}'

    class Meta:
        verbose_name = 'Коментарий продукта'
        verbose_name_plural = 'Коментарии продукта'