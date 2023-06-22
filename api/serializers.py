from rest_framework import serializers
from blog.models import ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model=ArticleModel
		exclude=['created','updated']