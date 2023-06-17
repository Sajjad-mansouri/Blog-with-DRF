from django.urls import path
from . import views

app_name='account'
urlpatterns=[
	path('',views.ProfileView.as_view(),name='profile'),
	path('create-article/',views.CreateArticle.as_view(),name='create-article'),
	path('articles-list/',views.ProfileArticleList.as_view(),name='articles-list'),

]