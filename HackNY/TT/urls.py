from django.conf.urls import patterns, url
from TT import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)