from twython import Twython
from pprint import pprint
from textblob import TextBlob
import json

APP_KEY = "Qn4Nx6C9LtoAlKtYLtoNQX2uY"
APP_SECRET = "mFk56Ec74tSW74Dp8uQqmyxMHKVeMAgQU8cLjRFqV3Ro87cSiN"

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
twitter_json = twitter.search(q='python', count = 100)

data = []
for status in twitter_json['statuses']:
    text = status['text']
    blob = TextBlob(text)
    dic = {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity }
    data.append(dic)

JSON = json.dumps(data)
