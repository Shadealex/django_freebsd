"""billing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from foto.views import current_datetime, photo_index, duty, album_1, album_2, test_page
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^1/', current_datetime),
    url(r'^2/', duty),
    url(r'^test', test_page),
    url(r'^portfolio_one.html', album_1),
    url(r'^portfolio_two.html', album_2),
    url(r'^', photo_index),
] + static(settings.STATIC_URL,)


# urlpatterns = patterns('',
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^1/', current_datetime),
#     url(r'^2/', photo_index),
#     url(r'^', duty),
#     )
# if settings.DEBUG:
#     urlpatterns += patterns('',
#         url(r'^search/(?P.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#     )
