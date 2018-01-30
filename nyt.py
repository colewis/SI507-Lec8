#ny-simple.py
from secrets import *
import requests
import nytcache


# gets stories from a particular section of NY times
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': nyt_key}
    return nytcache.make_request_using_cache(extendedurl, params)

def get_headlines(nyt_results_dict):
    results = nyt_results_dict['results']
    headlines = []
    for r in results:
        headlines.append(r['title'])
    return headlines

story_list_json = get_stories('science')
#print(story_list_json)
headlines = get_headlines(story_list_json)
for h in headlines:
    print(h)
