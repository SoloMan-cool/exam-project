from django.contrib import admin
from .models import Cart, CartProduct
from unfold.admin import ModelAdmin, TabularInline


class CartProductInline(TabularInline):
    model = CartProduct



@admin.register(Cart)
class CartAdmin(ModelAdmin):
    inlines = [CartProductInline]