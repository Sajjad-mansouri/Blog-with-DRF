from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager

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
	tags = TaggableManager()

	objects=models.Manager()
	publish_manager=PublishedManger()

	def __str__(self):
		return self.title



class CommentModel(models.Model):
	post=models.ForeignKey(ArticleModel,related_name='comments',on_delete=models.CASCADE)
	name=models.CharField(max_length=50)
	body=models.TextField()
	email=models.EmailField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)

	def __str__(self):
		return f'{self.post}'
