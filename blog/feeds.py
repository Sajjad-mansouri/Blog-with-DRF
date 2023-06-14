from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from .models import ArticleModel


class BlogFeed(Feed):
	title='Blog Feeds'

	#link='/link'
	#http://localhost:8000/link
	link='/'
	description='this is blog website'

	def items(self):
		return ArticleModel.publish_manager.all()[:4]
	def item_title(self,item):
		return item.title
	def item_description(self,item):
		return truncatewords(item.content,30)

	def item_link(self, item):
		print('slug:       ',item.slug)
		return reverse("blog:article-detail", kwargs={'slug':item.slug})