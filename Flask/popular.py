from urllib2 import urlopen
from json import loads
import codecs

def call_the_articles():
    url = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/30.json?&offset=%s&api-key=a1f2de9c74a24d2cf3f72d910ff68018:14:61296924"
    return loads(urlopen(url).read())
    
articles = call_the_articles()

article_file = codecs.open('output.txt', 'w', encoding='utf-8')
for article in articles["results"]:
    article_file.write(article["title"] + "\n")
    
article_file.close()