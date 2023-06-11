from django import forms

class ContactForm(forms.Form):
	first_name=forms.CharField(max_length=100)
	last_name=forms.CharField(max_length=100)
	email=forms.EmailField()
	content=forms.CharField(widget=forms.TextInput())