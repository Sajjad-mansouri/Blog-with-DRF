from rest_framework import serializers
from django.contrib.auth import get_user_model
from blog.models import ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model=ArticleModel
		exclude=['created','updated']

	def validate_title(self,value):
		filter_list=['forbidden']
		for item in filter_list:
			if item in value:
				raise serializers.ValidationError(f"{item} don't allowed")

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=get_user_model()
		fields='__all__'