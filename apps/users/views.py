from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist, WishlistItem
from apps.shop.models import Product

# Create your views here.
def show_auth_page(request):
    return render(request, 'users/auth.html')

@login_required(login_url='auth-page')
def show_wishlist_page(request):
    user_wishlist = Wishlist.objects.filter(user=request.user).first()
    context = {
        'user_wishlist': user_wishlist
    }

    return render(request, 'users/wishlist.html', context)

def add_or_delete_wishlist_item(request, product_slug):
    user_wishlist = Wishlist.objects.filter(user=request.user).first()
    user_wishlist_products = [item.product for item in user_wishlist.wishlist_items.all()]
    product = Product.objects.get(slug=product_slug)

    if product not in user_wishlist_products:
        WishlistItem.objects.create(wishlist=user_wishlist, product=product)
    else:
        item = WishlistItem.objects.get(wishlist=user_wishlist, product=product)
        item.delete()

    return redirect('wishlist')