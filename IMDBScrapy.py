from bs4 import BeautifulSoup
import requests
import re
import json

# get number of seasons of a tv show
def numberofseasons():
    URL = 'https://www.imdb.com'
    newURL = URL + '/title/tt0092455/'
    page = requests.get(newURL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='title-episode-widget')

    seasonlist = results.find_all('a', href = True)

    for i in seasonlist:
        if "season=" not in i:
            seasonlist.pop()

    numSeasons = len(seasonlist)
    #print(numSeasons)
    return numSeasons

numberofseasons()

def seasonratings(seasonid):
    URL = 'https://www.imdb.com'
    newURL = URL + '/title/tt0092455/episodes?season=' + str(seasonid)
    page = requests.get(newURL)

    soup = BeautifulSoup(page.content, 'html.parser')

    episodelist = []
    for episode in soup.find_all('strong'):
        if "/title/" in str(episode):               #this possibly could've been replaced by soup.get('href')
            episode = re.findall(r'"([^"]*)"', str(episode))
            episodelist.append(episode[0])

    URLnew = ''
    epinfoJSON = []
    for episode in episodelist:
        URLnew = URL + episode
        #print(URLnew)
        page = requests.get(URLnew)

        soup = BeautifulSoup(page.content, 'html.parser')

        epinfoJSON.append(json.loads(soup.find('script', type="application/ld+json").text))

    for i, k in enumerate(epinfoJSON):
        if "season" not in k.keys():
            k["season"] = seasonid
        if "episode" not in k.keys():
            k["episode"] = (i+1)
        k.pop("@context", None)
        k.pop("@type", None)
        k.pop("image", None)
        k.pop("contentRating", None)
        k.pop("actor", None)
        k.pop("director", None)
        k.pop("creator", None)
        k.pop("description", None)
        k.pop("datePublished", None)
        k.pop("keywords", None)
        k.pop("review", None)
        k.pop("timeRequired", None)
        k.pop("trailer", None)

    #print(epinfoJSON)
    return epinfoJSON

#seasonratings(1)
def showratingaggregate():
    seriesaggregateratingslist = []
    for i in range(1,numberofseasons()+1):
        seriesaggregateratingslist.append(seasonratings(i))

    #print(seriesaggregateratingslist)
    return seriesaggregateratingslist

    """u = 0

    for dict in seriesaggregateratingslist:
        for doubledict in dict:
            u += 1
    print(u)"""

#print(type(showratingaggregate()))
