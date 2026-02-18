from itertools import product
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Category, Product, Shop

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
    categories = Category.objects.all().order_by('id')
    products = Product.objects.all()
    shops = Shop.objects.all()

    paginator = Paginator(products, 6)  # 👈 6 товаров на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'shops': shops,
        'page_obj': page_obj,
    }

    return render(request, 'shop/shop.html', context)

def show_product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    products = Product.objects.all()

    context = {
        'product': product,
        'products': products,
    }
    return render(request, 'shop/product.html', context)