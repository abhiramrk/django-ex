from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, login, health, profile

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^login$', login),
    url(r'^health$', health),
    url(r'^profile$', profile),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
]
