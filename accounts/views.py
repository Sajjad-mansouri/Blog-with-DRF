from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from blog.models import ArticleModel
from .forms import ArticleForm


class ProfileView(LoginRequiredMixin,TemplateView):

	template_name='accounts/profile.html'



class CreateArticle(CreateView):
	model=ArticleModel
	template_name='blog/create-update-article.html'
	success_url=reverse_lazy('account:profile')
	form_class=ArticleForm

	def form_valid(self,form):
		self.object=form.save(commit=False)
		self.object.author=self.request.user
		self.object.save()
		return redirect('account:profile')

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request':self.request})
		return kwargs
