from django.urls import path, include
from .views import (BooksListView, BookDetailView, SignUpView, profile,
    all_cart, add_to_cart, delete_from_cart, delete_cart, delete_all_cart,
    orderCreate, OrderUpdate)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile', profile, name='profile'),
    path('', (BooksListView.as_view()), name='book-list'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
