from django.db import models
from django.conf import settings
from django.utils import timezone

class PublishedManger(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status=True)

class ArticleModel(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField(max_length=100,unique=True)
	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	content=models.TextField()
	image=models.ImageField(upload_to='images/%Y/%m/',null=True,blank=True)
	published=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.BooleanField(default=False)

	objects=models.Manager()
	publish_manager=PublishedManger()

	def __str__(self):
		return self.title
