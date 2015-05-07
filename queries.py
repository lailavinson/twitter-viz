from twython import Twython
from pprint import pprint
from textblob import TextBlob
import json

APP_KEY = "Qn4Nx6C9LtoAlKtYLtoNQX2uY"
APP_SECRET = "mFk56Ec74tSW74Dp8uQqmyxMHKVeMAgQU8cLjRFqV3Ro87cSiN"
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

query = 'python'
nTweets = 100
noRetweets = True

# Single query
def single_query(query=query, count=nTweets):
    if(noRetweets):
        query += " -'RT @'"
    twitter_json = twitter.search(q = query, count = nTweets)
    data = []
    for status in twitter_json['statuses']:
        text = status['text']
        blob = TextBlob(text)
        dic = {
            'polarity': blob.sentiment.polarity, 
            'subjectivity': blob.sentiment.subjectivity,
            'text': text
        }
        data.append(dic)
    # JSON = json.dumps(data)
    return data



#Multiple queries
# nTweets = 2
queries = ['ucla', 'usc']

def multi_query(query=queries, count=nTweets):
twitter_jsons = []
for query in queries:
    if(noRetweets):
        query += " -'RT @'"
    results = twitter.search(q = query, count = nTweets)
    twitter_jsons.append(results)

data = []
for twitter_json in twitter_jsons:
    curr_data = []
    for status in twitter_json['statuses']:
        text = status['text']
        blob = TextBlob(text)
        dic = {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity }
        curr_data.append(dic)
	wrapper = { twitter_json['search_metadata']['query']: curr_data }
    data.append(wrapper)

JSON = json.dumps(data)


# Geocode query
geo = '34.07098,-118.4448,1mi' # 1mi radius around UCLA
# nTweets = 100

def geo_query(query=query, geocode=geo, count=100):
    if(noRetweets):
        query += " -'RT @'"
    twitter_json = twitter.search(q = query, geocode = geocode, count = count)
    data = []
    for status in twitter_json['statuses']:
        text = status['text']
        blob = TextBlob(text)
        dic = {
            'polarity': blob.sentiment.polarity, 
            'subjectivity': blob.sentiment.subjectivity,
            'text': text
            }
        data.append(dic)
    #JSON = json.dumps(data)
    return data
