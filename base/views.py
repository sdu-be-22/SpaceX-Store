from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView
)
from .filters import BookFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django import forms
from django.db.models import Sum
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CommentModelForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = [
			'text',
		]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email' , 'first_name','last_name' ]
