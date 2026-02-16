from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Shop, Tags, Products


@admin.register(Shop)
class ShopAdmin(ModelAdmin):
    list_display = ['name',]


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Tags)
class TagsAdmin(ModelAdmin):
    list_display = ['name',]

@admin.register(Products)
class ProductsAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'status', 'price', 'status']
    list_filter = ['created_at']