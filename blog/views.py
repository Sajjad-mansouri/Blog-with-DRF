from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic import FormView
from django.urls import reverse_lazy,reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Count
from .forms import ContactForm,CommentForm
from .models import ArticleModel
from taggit.models import Tag

class ArticleListView(ListView):
	model=ArticleModel
	def get_queryset(self):
		
		queryset=super().get_queryset()
		try:
			tags=self.kwargs['tags']
			tags=Tag.objects.get(slug=tags)
			return queryset.filter(tags__in=[tags])

		except:
			return queryset.filter(status=True)
	def get_context_data(self,**kwargs):
		kwargs= super().get_context_data(**kwargs)
		try:
			kwargs['tags']=self.kwargs['tags']
		except:
			pass
		return kwargs
	template_name='blog/list.html'
	paginate_by=3

	

class ArticleDetailView(FormView):
	
	template_name='blog/detail.html'
	form_class=CommentForm

	def get_context_data(self,**kwargs):
		slug=self.kwargs['slug']
		if "form" not in kwargs:
			kwargs["form"] = self.get_form()
		object=ArticleModel.objects.get(slug=slug)
		tags_id=object.tags.values_list('id',flat=True)
		similar_articles=ArticleModel.publish_manager.filter(tags__id__in=tags_id).exclude(id=object.id)

		similar_articles=similar_articles.annotate(count=Count('tags')).order_by('-count','-published')
		kwargs['similar_articles']=similar_articles
		kwargs['object']=object
		kwargs['comments']=object.comments.filter(active=True)
		
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		"""If the form is valid, redirect to the supplied URL."""
		form.save()
		return HttpResponseRedirect(reverse('blog:article-detail',kwargs={'slug':self.kwargs['slug']}))


class ContactView(FormView):
	form_class=ContactForm
	template_name='blog/contact-form.html'
	success_url = reverse_lazy('blog:articles-list')





