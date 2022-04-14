import django_filters
from .models import Book
from django import forms

class BookFilter(django_filters.FilterSet):
	name=django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
            'placeholder': 'поиск...', 'class': 'form-control mb-2 mr-sm-2'})) 
	class Meta:
		model = Book
		fields = ['name', 'genre']


