from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_auth_page, name='auth-page'),
    path('wishlist/', views.show_wishlist_page, name='wishlist-page'),
    path('wishlist/<slug:product_slug>/', views.add_or_delete_wishlist_item, name='wishlist-action'),
]