from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin, TabularInline
from .models import User, WishlistItem, Wishlist


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

class WishlistItemInline(TabularInline):
    model = WishlistItem
    extra = 1

@admin.register(Wishlist)
class WishlistAdmin(ModelAdmin):
    inlines = [WishlistItemInline]

