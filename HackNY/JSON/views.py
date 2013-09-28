from django.http import HttpResponse
import datetime
import json
import urllib2

articleSearch = "895b5c2b2d01446ed289e27f8efadd91:6:67424427"

def news(request):
	response = urllib2.urlopen('http://api.nytimes.com/svc/search/v2/articlesearch.response-format?json&query=obama&api-key=%s') % articleSearch
	return HttpResponse(json.dumps(response), content_type="application/json")