from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from blog.models import ArticleModel
from .forms import ArticleForm,AuthorForm
from .mixins import AuthorMixin,AuthorQueryset,RequestFormKwarg


class ProfileView(LoginRequiredMixin,TemplateView):

	template_name='accounts/profile.html'


class ProfileArticleList(LoginRequiredMixin,AuthorQueryset,ListView):
	template_name='accounts/articles-list.html'
	def get_queryset(self):
		return ArticleModel.publish_manager.filter(author=self.request.user)



class CreateArticle(LoginRequiredMixin,AuthorMixin,CreateView):
	model=ArticleModel
	template_name='blog/create-update-article.html'
	success_url=reverse_lazy('account:profile')
	form_class=ArticleForm




class UpdateArticle(LoginRequiredMixin,AuthorQueryset,AuthorMixin,UpdateView):
	template_name='blog/create-update-article.html'
	form_class=ArticleForm


class AccountDetail(LoginRequiredMixin,DetailView):
	template_name='accounts/account.html'
	def get_object(self):
			return get_user_model().objects.get(username=self.request.user.username)
	
class AccountUpdate(LoginRequiredMixin,RequestFormKwarg,UpdateView):
	template_name='accounts/account.html'
	form_class=AuthorForm
	success_url=reverse_lazy('account:account-detail')
	def get_object(self):
			return get_user_model().objects.get(username=self.request.user.username)