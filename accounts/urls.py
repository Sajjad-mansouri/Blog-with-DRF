from django.urls import path
from . import views

app_name='account'
urlpatterns=[
	path('',views.ProfileView.as_view(),name='profile'),
	path('articles-list/',views.ProfileArticleList.as_view(),name='articles-list'),
	path('create-article/',views.CreateArticle.as_view(),name='create-article'),
	path('update-article/<int:pk>/',views.UpdateArticle.as_view(),name='update-article'),
	path('account/delete/article/<pk>',views.ArticleDelete.as_view(),name='article-delete'),

	#account
	path('account/',views.AccountDetail.as_view(),name='account-detail'),
	path('account/update/',views.AccountUpdate.as_view(),name='account-update'),



]