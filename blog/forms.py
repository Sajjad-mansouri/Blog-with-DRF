from django import forms
from .models import CommentModel

class ContactForm(forms.Form):
	first_name=forms.CharField(max_length=100)
	last_name=forms.CharField(max_length=100)
	email=forms.EmailField()
	content=forms.CharField(widget=forms.TextInput())


class CommentForm(forms.ModelForm):
	class Meta:
		model=CommentModel
		fields=['post', 'name', 'body', 'email']