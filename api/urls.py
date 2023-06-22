from django.urls import path,include
from . import views
urlpatterns=[
	#blog
	path('',views.ArticleAPIList.as_view(),name='article-list'),
	path('article/<slug:slug>/',views.ArticleAPIDetail.as_view(),name='article-Detail'),

	#user
	path('users/',views.UserAPIList.as_view(),name='user-list'),
	path('user/<int:pk>/',views.UserAPIDetail.as_view(),name='user-detail'),






	#authentication
	path('api-auth/', include('rest_framework.urls')),
]