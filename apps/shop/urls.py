from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_home_page, name='home-page'),
    path('shop/', views.show_shop_page, name='shop-page'),
]
