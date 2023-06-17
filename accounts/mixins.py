from django.shortcuts import redirect
from blog.models import ArticleModel





class RequestFormKwarg:
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request':self.request})
		return kwargs	

class AuthorQueryset:
	def get_queryset(self):
		return ArticleModel.publish_manager.filter(author=self.request.user)

class AuthorMixin(RequestFormKwarg):

	def form_valid(self,form):
		self.object=form.save(commit=False)
		self.object.author=self.request.user
		self.object.save()
		form.save_m2m()
		return redirect('account:profile')




