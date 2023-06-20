from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.utils.encoding import force_bytes
from django.http import Http404
from .forms import UserRegisterForm

default_token_generator= PasswordResetTokenGenerator()

UserModel = get_user_model()
class RegisterUser(CreateView):
	form_class=UserRegisterForm
	template_name='users/register.html'
	def dispatch(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			raise Http404
		return super().dispatch(request,*args,**kwargs)

	def form_valid(self,form):
		user = form.save(commit=False)
		user.is_active = False
		user.save()	
		current_site = get_current_site(self.request)
		site_name = current_site.name
		domain = current_site.domain
		subject_template_name='users/password_reset_subject.txt'
		mail_subject=render_to_string(subject_template_name,{'site_name':site_name})
		token=default_token_generator.make_token(user)
		uid=urlsafe_base64_encode(force_bytes(user.pk))
		message=render_to_string('users/activate_email.html',{
			'user':user,
			'current_site':current_site,
			'site_name':site_name,
			'uid':uid,
			'token':token
			})
		to_email=form.cleaned_data.get('email')
		email=EmailMessage(mail_subject,message,to=[to_email])
		email.send()
		return redirect('user:register-done')

class RegisterDone(TemplateView):
	template_name='users/registration-done.html'


def activate(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = UserModel.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
		user = None
	if user is not None and default_token_generator.check_token(user, token):
		user.is_active = True
		user.save()
		
		return render(request,'users/registration-complete.html',{
 					"title":"Registration succussfully done.",
 					"validlink": True,
 				})
	else:
		return render(request,'users/registration-complete.html',{
 					"title":"Registration unseccussful",
 					"validlink": False,
 				})



# class ActivateView(TemplateView):
# 	template_name='users/registration-done.html'
# 	token_generator = default_token_generator


# 	def get_user(self, uidb64):
# 		try:
# 			# urlsafe_base64_decode() decodes to bytestring
# 			uid = urlsafe_base64_decode(uidb64).decode()
# 			user=get_user_model().objects.get(pk=uid)
# 			# user = UserModel._default_manager.get(pk=uid)
# 		except (
# 			TypeError,
# 			ValueError,
# 			OverflowError,
# 			UserModel.DoesNotExist,
# 			ValidationError,
# 		):
# 			user = None
# 		return user
# 	def dispatch(self,request,*args,**kwargs):

# 		if "uidb64" not in kwargs or "token" not in kwargs:
# 			raise ImproperlyConfigured(
# 				"The URL path must contain 'uidb64' and 'token' parameters."
# 			)

# 		self.validlink = False
# 		self.user = self.get_user(kwargs["uidb64"])
# 		if self.user is not None:
# 			token = kwargs["token"]
# 			if self.token_generator.check_token(self.user, token):
# 					self.validlink = True
# 					self.user.is_active=True
# 					return super().dispatch(request,*args, **kwargs)
# 		return self.render_to_response(self.get_context_data())

# 	def get_context_data(self,**kwargs):
# 		context = super().get_context_data(**kwargs)
# 		if self.validlink:
# 			context.update(
# 				{
# 					"title":"Registration succussfully done.",
# 					"validlink": True,
# 				}
# 			)	

# 		else:
# 			context.update(
# 				{
# 					"title":"Registration unsuccussfully",
# 					"validlink": False,
# 				}
# 			)
# 		return context			

