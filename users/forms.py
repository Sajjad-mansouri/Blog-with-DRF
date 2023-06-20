from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import User

class UserRegisterForm(UserCreationForm):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['password1'].help_text=None

	class Meta:
		model=User
		fields = ('username','email','profile_image', 'password1', 'password2')