from django.db import models
from apps.common.models import BaseTimedModel


class Cart(BaseTimedModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')

    def get_cart_total_price(self):
        cart_products = self.cart_products.all()
        return sum([cart_product.get_total_price() for cart_product in cart_products])

    def get_cart_total_price_with_sale(self):
        cart_products = self.cart_products.all()
        return sum([cart_product.get_total_price_with_discount() for cart_product in cart_products])

    def get_cart_total_quantity(self):
        return sum([i.quantity for i in self.cart_products.all()])

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

    def get_total_price_with_discount(self):
        return self.product.get_price() * self.quantity