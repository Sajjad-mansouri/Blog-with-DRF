from django import forms
from blog.models import ArticleModel


class ArticleForm(forms.ModelForm):
	class Meta:
		model=ArticleModel

		exclude=['author']
