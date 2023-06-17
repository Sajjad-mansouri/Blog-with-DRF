from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from blog.models import ArticleModel
from .forms import ArticleForm


class ProfileView(LoginRequiredMixin,TemplateView):

	template_name='accounts/profile.html'


class ProfileArticleList(LoginRequiredMixin,ListView):
	template_name='accounts/articles-list.html'
	def get_queryset(self):
		return ArticleModel.publish_manager.filter(author=self.request.user)


class CreateArticle(LoginRequiredMixin,CreateView):
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


class UpdateArticle(LoginRequiredMixin,UpdateView):
	template_name='blog/create-update-article.html'
	fields='__all__'
	def get_queryset(self):

		return ArticleModel.publish_manager.filter(author=self.request.user)
