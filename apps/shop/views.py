from itertools import product

from django.shortcuts import render
from .models import Category, Tags, Product, Shop

# Create your views here.
def show_home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/index.html', context)

def show_shop_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    shops = Shop.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'shops': shops,
    }

    return render(request, 'shop/shop.html', context)

