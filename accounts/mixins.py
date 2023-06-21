from django.shortcuts import redirect
from blog.models import ArticleModel
from django.http import Http404,HttpResponseRedirect





class RequestFormKwarg:
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request':self.request})
		return kwargs	

class AuthorDispatch:
	def dispatch(self,request,*args,**kwargs):
		if (request.user.is_authenticated and request.user.is_author) or request.user.is_superuser:
			return super().dispatch(request,*args,**kwargs)
		else:
			raise Http404
class SuperUserDispatch:
	def dispatch(self,request,*args,**kwargs):
		if  request.user.is_superuser:
			return super().dispatch(request,*args,**kwargs)
		else:
			raise Http404	
class AuthorQueryset(AuthorDispatch):
	def get_queryset(self):
		if self.request.user.is_superuser:
			return ArticleModel.publish_manager.all()
		else:

			return ArticleModel.publish_manager.filter(author=self.request.user)



class AuthorMixin(AuthorDispatch,RequestFormKwarg):
	def form_valid(self,form):
		self.object=form.save(commit=False)
		self.object.author=self.request.user
		self.object.save()
		form.save_m2m()
		return HttpResponseRedirect(self.get_success_url())




