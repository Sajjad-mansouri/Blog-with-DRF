from django import forms
from blog.models import ArticleModel


class ArticleForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super().__init__(*args, **kwargs)
		self.fields['author'].initial = self.request.user
		self.fields['author'].disabled=True


	class Meta:
		model=ArticleModel
		fields='__all__'
