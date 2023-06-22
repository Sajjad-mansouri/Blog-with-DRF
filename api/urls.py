from django.urls import path,include
from . import views
urlpatterns=[
	path('',views.ArticleAPIList.as_view(),name='article-list'),
	path('api-auth/', include('rest_framework.urls')),
]