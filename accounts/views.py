from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from blog.models import ArticleModel
from .forms import ArticleForm
from .mixins import AuthorMixin


class ProfileView(LoginRequiredMixin,TemplateView):

	template_name='accounts/profile.html'


class ProfileArticleList(LoginRequiredMixin,ListView):
	template_name='accounts/articles-list.html'



class CreateArticle(LoginRequiredMixin,AuthorMixin,CreateView):
	model=ArticleModel
	template_name='blog/create-update-article.html'
	success_url=reverse_lazy('account:profile')
	form_class=ArticleForm




class UpdateArticle(LoginRequiredMixin,AuthorMixin,UpdateView):
	template_name='blog/create-update-article.html'
	form_class=ArticleForm

