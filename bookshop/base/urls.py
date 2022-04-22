from django.urls import path, include
from .views import (BooksListView, BookDetailView, SignUpView, profile,
    all_cart, add_to_cart, delete_from_cart, delete_cart, delete_all_cart,
    orderCreate, OrderUpdate)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile', profile, name='profile'),
