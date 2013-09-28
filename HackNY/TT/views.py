from django.http import HttpResponse
import datetime
import json

def index(request):
	now = datetime.datetime.now()
	html = "<html><head></head><body>hello %s</body></html>" %now
	return HttpResponse(html)

def news(request):
	