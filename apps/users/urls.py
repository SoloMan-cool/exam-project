from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_auth_page, name='auth-page'),
]