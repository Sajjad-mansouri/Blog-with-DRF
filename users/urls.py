from django.urls import path
from . import views 

app_name='user'
urlpatterns=[

    # path('register/',RegisterUser.as_view(),name='register'),
    path('register/',views.RegisterUser.as_view(),name='register'),
    path('register/done',views.RegisterDone.as_view(),name='register-done'),
    path('register/confirm/<uidb64>/<token>/',views.activate,name='register-confirm')
]


