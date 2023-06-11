
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('contact/',ContactView.as_view(),name='contact'),
    path('account/',include('django.contrib.auth.urls')),
    path('profile/',include('accounts.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)