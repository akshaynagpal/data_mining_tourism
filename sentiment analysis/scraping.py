import urllib2
from bs4 import BeautifulSoup

def get_page(page):
    response = urllib2.urlopen(page)
    html = response.read()
    return html

markup = get_page("http://topsy.com/s?q=weather%2C%20delhi&type=tweet&language=en&mintime=1230773459&maxtime=1262223025&offset=0")

soup = BeautifulSoup(markup)

for x in soup:
    print x
