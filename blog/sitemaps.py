from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from blog.models import ArticleModel

class BlogSitemap(Sitemap):
	# changefreq = "weekly"
	priority = 0.5

	def items(self):
		return ArticleModel.publish_manager.all()

	def lastmod(self, obj):
		return obj.published

	def location(self,obj):
		return reverse('blog:article-detail',kwargs={'slug':obj.slug})

	def changefreq(self,obj):
		updated=obj.updated
		now=timezone.now()
		change_time=(now-updated).total_seconds()

		if change_time/3600 <1:
			return 'always'
		elif 1<=change_time/3600<24:
			return 'hourly'
		elif 1<= change_time/(3600*24) <= 7:
			return 'weekly'
		elif 30<= change_time/(3600*24) <= 360:
			return 'yearly'
		else:
			return 'never'


class StaticViewSitemap(Sitemap):
	priority = 0.5
	changefreq = "daily"

	def items(self):
		return ["contact",]

	def location(self, item):
		return reverse(item)