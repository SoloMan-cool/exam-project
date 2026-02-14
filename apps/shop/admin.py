from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Shop


@admin.register(Shop)
class ShopAdmin(ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}