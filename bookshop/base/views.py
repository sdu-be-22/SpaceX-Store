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
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.db.models import Sum
 
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'base/signup.html'
class BooksListView(ListView):
	model = Book
	template_name = 'base/list.html' 
	ordering = ['-pk']
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = BookFilter(self.request.GET, queryset = self.get_queryset())
		paginated_filtered_jobs = Paginator(context['filter'].qs, 32)
		page_number = self.request.GET.get('page')
		job_page_obj = paginated_filtered_jobs.get_page(page_number)
		context['book_page_obj'] = job_page_obj
		return context
