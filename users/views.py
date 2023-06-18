from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
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


	def form_valid(self, form):
		user=form.save(commit=False)
		user.is_active=False
		user.save()
		current_site = get_current_site(self.request)
		site_name = current_site.name
		domain = current_site.domain
		subject_template_name='users/password_reset_subject.txt'
		mail_subject=render_to_string(subject_template_name,{'site_name':site_name})
		token_generator= PasswordResetTokenGenerator()
		message=render_to_string('users/activision_email.html',{
			'user':user,
			'current_site':current_site,
			'site_name':site_name,
			'uid':urlsafe_base64_encode(force_bytes(user.pk)),
			'token':token_generator.make_token(user)
			})
		to_email=form.cleaned_data.get('email')
		email=EmailMessage(mail_subject,message,to=[to_email])
		email.send()
		return super().form_valid(form)