from flask import Flask
from flask import render_template
import json
import urllib2
import unicodedata
from flaskext.jsonify import jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/<topicname>")
def topic(topicname):
	data = urllib2.urlopen('http://192.237.242.72:8000/API/news.json/%s' % (article))
	j = json.load(data)
	print j
	articles = [
		{
			'title': "Hello",
			'text': "James",
			'url': "http://www.james.com"
		},
		{
			'title': "BYE",
			'text': "MAX",
			'url': "http://www.max.com"
		}
	]
	return render_template('article_t.html', articles = articles)

# API corrector
@app.route("/API/")
@app.route("/API/<name>")
def API(name):
	if name == "news.json":
		return "try news.json/Your Article Name"
	elif name == 'generaltags.json':
		return "try generaltags.json/Your Tag"
	else:
		return "try be cooler"

# Method to get the result from the search API
@app.route("/API/news.json/<articlename>")
@jsonify
def API_news(articlename):
	articleSearchAPI = "895b5c2b2d01446ed289e27f8efadd91:6:67424427"
	article = unicodedata.normalize('NFKD', articlename).encode('ascii','ignore')
	splitArray = article.split()
	article = "+".join(splitArray)
	data = urllib2.urlopen('http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=%s&api-key=%s' % (article, articleSearchAPI))
	j = json.load(data)
	return j

# Method to get general tags from the TimesTags API
@app.route("/API/generaltags.json/<tag>")
@jsonify
def API_Generaltag(tag):
	timesTagAPI = "184fb96d9f85459c3d044202ae46cd78:13:67424427"
	tagName = unicodedata.normalize('NFKD', tag).encode('ascii','ignore')
	data = urllib2.urlopen('http://api.nytimes.com/svc/suggest/v1/timestags?query=%s&api-key=%s' % (tagName, timesTagAPI))
	j = json.load(data)
	return j

# Method to get geographical news from the Geo API
@app.route("/API/geo.json/<geo>")
@jsonify
def API_Geotag(geo):
	timesTagAPI = "71b492f5c4449f568d5e64603c2ce0e5:9:67424427"
	geoName = unicodedata.normalize('NFKD', geo).encode('ascii','ignore')
	splitArray = geoName.split()
	geoName = "+".join(splitArray)
	data = urllib2.urlopen('http://api.nytimes.com/svc/semantic/v2/geocodes/query.json?name=%s&api-key=%s' % (geoName, timesTagAPI))
	j = json.load(data)
	return j

# Method to most popular news from the Most Popular News API
@app.route("/API/popular.json/<resource>/<sections>/<time>/<offset>")
@jsonify
def API_MostPopular(resource, sections, time, offset):
 	mostPopularAPI = "43adb49adb65435f07ccb0ed71e2e936:6:67424427"
 	allowedSections = ["Arts", "Automobiles","Autos","Books", "Booming","Business Day", "Corrections",
 					   "Crosswords Games", "Dining & Wine", "Education", "Fashion & Style", 
 					   "Great Homes and Destinations", "Health", "Home & Garden", "Job Market", 
 					   "Magazine", "Movies", "Multimedia", "N.Y. Region", "Opinion", "Real Estate",
 					   "Science", "Sports", "Style", "Sunday Review", "T:Style", "Technology", "Theater",
 					   "Travel", "U.S.", "World", "Your Money"]
 	sectionNames = ""	
 	numSections = len(sections)
 	numAllowedSections = len(allowedSections)
 	for index in range(0, numSections):
 		currentName = sections[index]
 		for allowedIndex in range(0, numAllowedSections):
 			if (currentName in allowedSections[allowedIndex]):
 				sections[index] = allowedSections[allowedIndex]
		if (currentName == sections[index]):
			print(currentName + "is not a valid section name.\n")

		if (numSections > 1 and index != numSections - 1):
			sectionNames += sections[index] + ";"
 	resourceType = unicodedata.normalize('NKFD', resource).encode('ascii', 'ignore')
 	sectionNames = unicodedata.normalize('NKFD', sectionNames).encode('ascii', 'ignore')
 	timePeriod = unicodedata.normalize('NKFD', time).encode('ascii', 'ignore')
 	numArticlesPerPage = unicodedata.normalize('NKFD', offset).encode('ascii', 'ignore')
 	data = urllib2.urlopen('http://api.nytimes.com/svc/mostpopular/v2/%s/%s/%s?offset=%s&api-key=%s' % (resourceType, sectionNames, timePeriod, numArticlesPerPage, mostPopularAPI))
 	j = json.load(data)
 	return j

if __name__ == "__main__":
    app.run(debug=True)
