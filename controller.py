from flask import Flask
from flask import render_template
from flask import request
from twython import Twython
from pprint import pprint
from textblob import TextBlob


APP_KEY = "Qn4Nx6C9LtoAlKtYLtoNQX2uY"
APP_SECRET = "mFk56Ec74tSW74Dp8uQqmyxMHKVeMAgQU8cLjRFqV3Ro87cSiN"


app = Flask(__name__)

@app.route('/')
@app.route('/', methods=['POST', 'GET'])
def home_page(name=None):
	return render_template('template.html', name=name)


@app.route('/submit', methods=['POST', 'GET'])
def process_query():
	error = None
	twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

	if request.method == 'POST':
		user_input = request.form["query"]

		twitter_json = twitter.search(q=user_input, count = 100)

		data = []
		for status in twitter_json['statuses']:
		    text = status['text']
		    blob = TextBlob(text)
		    dic = {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity }
		    data.append(dic)


	return render_template('results.html', results = data)
if __name__ == '__main__':
	app.run()