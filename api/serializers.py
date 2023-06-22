from rest_framework import serializers
from django.contrib.auth import get_user_model
from blog.models import ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model=ArticleModel
		exclude=['created','updated']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=get_user_model()
		fields='__all__'