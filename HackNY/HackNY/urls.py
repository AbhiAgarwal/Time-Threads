from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^API/', include('JSON.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('TT.urls')),
)
