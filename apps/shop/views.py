from django.shortcuts import render
from .models import Category

# Create your views here.
def show_home_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'shop/index.html', context)

def show_shop_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'shop/shop.html', context)