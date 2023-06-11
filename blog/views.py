from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import ArticleModel

class ArticleListView(ListView):
	queryset=ArticleModel.publish_manager.all()
	template_name='blog/list.html'
	paginate_by=3

class ArticleDetailView(DetailView):
	queryset=ArticleModel.publish_manager.all()
	template_name='blog/detail.html'



