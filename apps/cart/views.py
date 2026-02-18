from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.cart.models import Cart, CartProduct
from apps.shop.models import Product
from django.contrib import messages

@login_required(login_url='auth-page')
def show_cart_page(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    context = {
        'cart': cart
    }
    return render(request, 'cart/cart.html', context)

@login_required(login_url='auth-page')
def add_to_cart(request, product_slug, quantity=1):
    product = get_object_or_404(Product, slug=product_slug)
    quantity = int(request.POST.get('quantity', quantity))

    if quantity > product.quantity:
        messages.info(request, 'Нельзя добавить больше товара чем есть в наличии')
        return redirect(request.META.get('HTTP_REFERER', 'shop-page'))

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)

    cart_product.quantity += quantity
    cart_product.save()

    product.quantity -= quantity
    if product.quantity == 0:
        product.status = 'sold'
    product.save()

    messages.success(request, f'{product.name} добавлен в корзину')
    return redirect('cart-page')


@login_required(login_url='auth-page')
def remove_from_cart(request, cart_product_id):
    cart_product = get_object_or_404(CartProduct, id=cart_product_id, cart__user=request.user)
    product = cart_product.product

    product.quantity += cart_product.quantity
    if product.quantity > 0:
        product.status = 'new'
    product.save()

    cart_product.delete()
    messages.success(request, f'{product.name} удален из корзины')
    return redirect('cart-page')