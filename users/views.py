from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm

class RegisterUser(CreateView):
	template_name='users/register.html'
	form_class=UserRegisterForm
	success_url=reverse_lazy('login')