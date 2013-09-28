from django.http import HttpResponse
import datetime

JSON = {}

def index(request):
	now = datetime.datetime.now()
	html = "<html><head></head><body>hello %s</body></html>" % now
	return HttpResponse(html)