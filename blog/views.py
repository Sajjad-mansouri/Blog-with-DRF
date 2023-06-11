from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import ArticleModel

class ArticleListView(ListView):
	queryset=ArticleModel.publish_manager.all()
	template_name='blog/list.html'
	paginate_by=3

class ArticleDetailView(DetailView):
	queryset=ArticleModel.publish_manager.all()
	template_name='blog/detail.html'


class ContactView(FormView):
	form_class=ContactForm
	template_name='blog/contact-form.html'
	success_url = reverse_lazy('blog:articles-list')



