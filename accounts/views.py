from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from blog.models import ArticleModel
from .forms import ArticleForm,AuthorForm
from .mixins import AuthorMixin,AuthorQueryset,RequestFormKwarg,SuperUserDispatch


class ProfileView(LoginRequiredMixin,TemplateView):

	template_name='accounts/profile.html'


class ProfileArticleList(LoginRequiredMixin,AuthorQueryset,ListView):
	template_name='accounts/articles-list.html'


class CreateArticle(LoginRequiredMixin,SuccessMessageMixin,AuthorMixin,CreateView):
	model=ArticleModel
	template_name='blog/create-update-article.html'
	success_url=reverse_lazy('account:articles-list')
	form_class=ArticleForm
	success_message='<<%(title)s>> article be created'
	def get_success_message(self,cleaned_data):
		return self.success_message % dict(cleaned_data)



class UpdateArticle(LoginRequiredMixin,AuthorQueryset,SuccessMessageMixin,AuthorMixin,UpdateView):
	template_name='blog/create-update-article.html'
	form_class=ArticleForm
	success_url=reverse_lazy('account:articles-list')
	success_message='<<%(obj)s>> article be updated'
	def form_valid(self,form):
		super().form_valid(form)
		if form.has_changed():
			messages.success(self.request, "Your profile was updated.")

	def get_success_message(self,cleaned_data):
		return self.success_message % dict(obj=self.object.title)

class AccountDetail(LoginRequiredMixin,DetailView):
	template_name='accounts/account.html'
	def get_object(self):
			return get_user_model().objects.get(username=self.request.user.username)
	
class AccountUpdate(LoginRequiredMixin,RequestFormKwarg,SuccessMessageMixin,UpdateView):
	template_name='accounts/account.html'
	form_class=AuthorForm
	success_url=reverse_lazy('account:account-detail')
	success_message='account be updated'

	def get_object(self):
			return get_user_model().objects.get(username=self.request.user.username)


class ArticleDelete(LoginRequiredMixin,SuperUserDispatch,SuccessMessageMixin,DeleteView):
	template_name='accounts/article_confim_delete.html'
	model=ArticleModel
	success_url=reverse_lazy('account:articles-list')
	success_message='<<%(obj)s>> article was deleted'
	def get_success_message(self,cleaned_data):
		return self.success_message % dict(obj=self.object.title)