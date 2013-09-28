from django.conf.urls import patterns, url
from JSON import views

urlpatterns = patterns('',
    url(r'^news.json', views.news, name='news')
)