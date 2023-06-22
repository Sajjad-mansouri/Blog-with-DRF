
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views
from blog.views import ContactView
from blog.sitemaps import BlogSitemap,StaticViewSitemap
from blog.feeds import BlogFeed


sitemaps={
    'blog':BlogSitemap,
    'static':StaticViewSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('contact/',ContactView.as_view(),name='contact'),
    path('account/',include('django.contrib.auth.urls')),
    path('profile/',include('accounts.urls')),
    path('feeds/',BlogFeed(),name='feeds'),
    #user registration
    path('user/',include('users.urls')),

    #sitemap
    path(
        "sitemap.xml",
        views.index,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.index",
        ),
    path(
        "sitemap-<section>.xml",
        views.sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
        
        ),
   


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



 #DRF
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]