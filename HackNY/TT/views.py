from django.http import HttpResponse
import datetime
import json
import urllib2

articleSearch = "895b5c2b2d01446ed289e27f8efadd91:6:67424427"

def index(request):
	now = datetime.datetime.now()
	html = "<html><head></head><body>hello %s</body></html>" % now
	return HttpResponse(html)

def news(request):
	response = urllib2.urlopen('https://api.instagram.com/v1/tags/pizza/media/XXXXXX')