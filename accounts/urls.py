from django.urls import path
from . import views

app_name='account'
urlpatterns=[
	path('',views.ProfileView.as_view(),name='profile')
]