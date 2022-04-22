from django.urls import path, include
from .views import (BooksListView, BookDetailView, SignUpView, profile,
    all_cart, add_to_cart, delete_from_cart, delete_cart, delete_all_cart,
    orderCreate, OrderUpdate)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile', profile, name='profile'),
    path('', (BooksListView.as_view()), name='book-list'),
    path('book/<int:pk>', (BookDetailView.as_view()), name='book-detail'),
    path('cart/list', all_cart, name='cart-list'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add-to-cart'),
    path('delete_from_cart/<int:pk>', delete_from_cart, name='delete-from-cart'),
    path('delete_cart/<int:pk>', delete_cart, name='delete-cart'),
    path('delete_all_cart/', delete_all_cart, name='delete-all-cart'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
