from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import ArticleSerializer
from blog.models import ArticleModel


class ArticleAPIList(ListAPIView):
	queryset = ArticleModel.objects.filter(status=True)
	serializer_class = ArticleSerializer
