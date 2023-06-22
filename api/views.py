from django.shortcuts import render
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import ArticleSerializer,UserSerializer
from blog.models import ArticleModel


class ArticleAPIList(generics.ListAPIView):
	queryset = ArticleModel.objects.filter(status=True)
	serializer_class = ArticleSerializer

class ArticleAPIDetail(generics.RetrieveAPIView):
	queryset = ArticleModel.objects.filter(status=True)
	# lookup_field='slug'
	multiple_lookup_fields=['slug',]
	serializer_class = ArticleSerializer

	def get_object(self):
		queryset = self.get_queryset()
		filter = {}
		for field in self.multiple_lookup_fields:
			filter[field] = self.kwargs[field]

		obj = get_object_or_404(queryset, **filter)
		self.check_object_permissions(self.request, obj)
		return obj


class UserAPIList(generics.ListCreateAPIView):
	queryset=get_user_model().objects.all()
	serializer_class = UserSerializer

class UserAPIDetail(generics.RetrieveAPIView):
	queryset=get_user_model().objects.all()
	serializer_class = UserSerializer