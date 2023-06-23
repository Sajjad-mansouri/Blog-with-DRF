from django.urls import path,include
from rest_framework.authtoken import views as auth_views
from rest_framework_simplejwt import views as jwt_views
from . import views
urlpatterns=[
	#blog
	path('',views.ArticleAPIList.as_view(),name='article-list'),
	path('article/<slug:slug>/',views.ArticleAPIDetail.as_view(),name='article-Detail'),

	#user
	path('users/',views.UserAPIList.as_view(),name='user-list'),
	path('user/<int:pk>/',views.UserAPIDetail.as_view(),name='user-detail'),

	#authentication

	#rest_framework.authentication.TokenAuthentication
	# path('api-token-auth/', auth_views.obtain_auth_token),
	
	#dj-rest-auth for login,logout,reset password and change password
	path('dj-rest-auth/', include('dj_rest_auth.urls')),
	#dj-rest-auth for registration
	path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

	#custom view
	path('destroy-token/',views.DestroyToken.as_view(),name='destroy-token'),
	#jwt
	path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),






	#authentication
	path('api-auth/', include('rest_framework.urls')),
]