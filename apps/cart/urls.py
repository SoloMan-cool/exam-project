from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_cart_page, name='cart-page'),
    path('add/<slug:product_slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove/<int:cart_product_id>/', views.remove_from_cart, name='delete-cart-product'),
    path('checkout/', views.show_checkout_page, name='checkout-page'),
]