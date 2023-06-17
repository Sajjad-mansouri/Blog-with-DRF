from django import forms
from blog.models import ArticleModel
from django.contrib.auth import get_user_model


class ArticleForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super().__init__(*args, **kwargs)
		self.fields['author'].initial = self.request.user
		self.fields['author'].disabled=True


	class Meta:
		model=ArticleModel
		fields='__all__'

class AuthorForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super().__init__(*args, **kwargs)
		self.fields['username'].initial = self.request.user.username
		self.fields['username'].disabled=True
		self.fields['email'].required=True



	class Meta:
		model=get_user_model()
		fields=['first_name','last_name','username','email','profile_image']