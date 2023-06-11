from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic import FormView
from django.urls import reverse_lazy,reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm,CommentForm
from .models import ArticleModel

class ArticleListView(ListView):
	queryset=ArticleModel.publish_manager.all()
	template_name='blog/list.html'
	paginate_by=3

class ArticleDetailView(FormView):
	
	template_name='blog/detail.html'
	form_class=CommentForm

	def get_context_data(self,**kwargs):
		slug=self.kwargs['slug']
		if "form" not in kwargs:
			kwargs["form"] = self.get_form()
		kwargs['object']=object=ArticleModel.objects.get(slug=slug)
		kwargs['comments']=object.comments.filter(active=True)
		
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		"""If the form is valid, redirect to the supplied URL."""
		form.save()
		return HttpResponseRedirect(reverse('blog:article-detail',kwargs={'slug':'second-article'}))


class ContactView(FormView):
	form_class=ContactForm
	template_name='blog/contact-form.html'
	success_url = reverse_lazy('blog:articles-list')



