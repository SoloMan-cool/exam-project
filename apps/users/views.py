from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist, WishlistItem
from apps.shop.models import Product
from .forms import UserAuthenticationForm, RegistrationForm
from django.contrib import messages
from apps.cart.models import Cart

# Create your views here.
def show_auth_page(request):
    auth_form = UserAuthenticationForm()
    registration_form = RegistrationForm()

    context = {
        'auth_form': auth_form,
        'registration_form': registration_form
    }

    return render(request, 'users/auth.html', context)

@login_required(login_url='auth-page')
def show_wishlist_page(request):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    context = {
        'wishlist_items': user_wishlist.wishlist_items.all()
    }

    return render(request, 'users/wishlist.html', context)

@login_required(login_url='auth-page')
def add_or_delete_wishlist_item(request, product_slug):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    product = Product.objects.get(slug=product_slug)

    item = WishlistItem.objects.filter(
        wishlist=user_wishlist,
        product=product
    ).first()

    if item:
        item.delete()
    else:
        WishlistItem.objects.create(
            wishlist=user_wishlist,
            product=product
        )

    return redirect('wishlist-page')

from django.contrib.auth import login, logout

def login_user(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт')
            return redirect('home-page')
        else:
            messages.error(request, 'Неверный логин или пароль')
    else:
        form = UserAuthenticationForm()

    return render(request, 'users/auth.html', {
        'auth_form': form,
        'registration_form': RegistrationForm()
    })


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save()

            Cart.objects.get_or_create(user=new_user)
            Wishlist.objects.get_or_create(user=new_user)

            login(request, new_user)

            messages.success(request, 'Аккаунт успешно создан')
            return redirect('home-page')
        else:
            messages.error(request, 'Ошибка при создании аккаунта')
    else:
        form = RegistrationForm()

    return render(request, 'users/auth.html', {
        'auth_form': UserAuthenticationForm(),
        'registration_form': form
    })

def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли с аккаунта')
    return redirect('home-page')