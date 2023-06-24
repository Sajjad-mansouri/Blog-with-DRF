from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin
from blog.models import ArticleModel

class AuthorField(serializers.RelatedField):
	def to_representation(self,value):
		return f'**{value.username}**'
class AuthorAPISerializer(serializers.ModelSerializer):
	class Meta:
		model=get_user_model()
		fields=['username','first_name','last_name']

class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
	# author=AuthorAPISerializer()
	# author=serializers.HyperlinkedIdentityField(view_name='users-detail',)
	# author=serializers.CharField(source='author.username',read_only=True)
	# author=AuthorField(read_only=True)
	def get_author(self,obj):
		return {
				'username':obj.author.username,
				'first name':obj.author.first_name,
				'last name':obj.author.last_name
		}
	author=serializers.SerializerMethodField('get_author')

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