from itertools import product
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Category, Product, Shop
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Count
from .forms import ProductReviewForm
from django.contrib import messages

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
    product = get_object_or_404(Product, slug=product_slug)
    reviews = product.reviews.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Комментарий успешно добавлен')
                return redirect('product-page', product_slug=product.slug)
        else:
            messages.error(request, 'Вы должны войти в систему')

    else:
        form = ProductReviewForm()

    similar_products = Product.objects.filter(
        tags__in=product.tags.all()
    ).exclude(
        slug=product_slug
    ).annotate(
        same_tags=Count('tags')
    ).order_by('-same_tags')[:4]

    context = {
        'product': product,
        'similar_products': similar_products,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'shop/detail.html', context)

def show_shop_page_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(categories=category).distinct()
    shops = Shop.objects.all()

    context = {
        'category': category,
        'products': products,
        'shops': shops,
    }

    return render(request, 'shop/category.html', context)