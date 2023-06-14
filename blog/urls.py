from django.urls import path
from .feeds import BlogFeed
from . import views

app_name='blog'

urlpatterns=[

	path('',views.ArticleListView.as_view(),name='articles-list'),
	path('tags/<tags>/',views.ArticleListView.as_view(),name='articles-tags'),
	path('detail/<slug:slug>/',views.ArticleDetailView.as_view(),name='article-detail'),
	path('feeds/',BlogFeed())
]