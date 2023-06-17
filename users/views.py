from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import Http404
from .forms import UserRegisterForm

class RegisterUser(CreateView):
	def dispatch(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			raise Http404
		return super().dispatch(request,*args,**kwargs)
	template_name='users/register.html'
	form_class=UserRegisterForm
	success_url=reverse_lazy('login')