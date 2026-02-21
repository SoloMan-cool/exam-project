from django.db import models
from apps.common.models import BaseTimedModel




class Cart(BaseTimedModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    def get_cart_total_price(self):
        cart_products = self.cart_products.all()
        return sum([cart_product.get_total_price() for cart_product in cart_products])

    def get_cart_total_price_with_discount(self):
        return sum(cart_product.total_price for cart_product in self.cart_products.all())

    def get_cart_total_quantity(self):
        return sum(cart_product.quantity for cart_product in self.cart_products.all())

    def __str__(self):
        return f'{self.user.username} cart'

    class Meta:
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзины пользователей'


class CartProduct(BaseTimedModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products',
                             verbose_name='Корзина пользователя')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во продукта')

    def get_total_price(self):
        return self.product.price * self.quantity

    @property
    def total_price(self):
        return self.product.discounted_price * self.quantity

class CheckoutForm(BaseTimedModel):
    name = models.CharField(verbose_name='Имя', max_length=50)
    lastname = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    company_name = models.CharField(verbose_name='Имя компании', max_length=50, null=True, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=50, null=True, blank=True)
    state = models.CharField(verbose_name='Штат/Страна', max_length=50, null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=50)
    address_line = models.CharField(verbose_name='Домашний аддресс', max_length=50)
    street_address = models.CharField(verbose_name='Доп аддресс', max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.lastname}'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['-created_at']