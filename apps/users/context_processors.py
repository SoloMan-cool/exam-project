from .models import Wishlist
from apps.cart.models import Cart

def wishlist_count(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user).first()
        if wishlist:
            return {
                'wishlist_count': wishlist.wishlist_items.count()
            }
    return {
        'wishlist_count': 0
    }

def base_context(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_count = cart.get_cart_total_quantity()
    return {'cart_count': cart_count}