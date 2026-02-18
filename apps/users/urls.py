from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_auth_page, name='auth-page'),
    path('auth/login/', views.login_user, name='login-user'),
    path('auth/register/', views.register_user, name='register-user'),
    path('auth/logout/', views.logout_user, name='logout-user'),
    path('wishlist/', views.show_wishlist_page, name='wishlist-page'),
    path('wishlist/<slug:product_slug>/', views.add_or_delete_wishlist_item, name='wishlist-action'),
]