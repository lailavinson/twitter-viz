from flask import Flask
from flask import render_template
from flask import request
from twython import Twython
from pprint import pprint
from textblob import TextBlob
import queries

# APP_KEY = "Qn4Nx6C9LtoAlKtYLtoNQX2uY"
# APP_SECRET = "mFk56Ec74tSW74Dp8uQqmyxMHKVeMAgQU8cLjRFqV3Ro87cSiN"


app = Flask(__name__)

@app.route('/')
@app.route('/', methods=['POST', 'GET'])
def home_page(name=None):
	return render_template('template.html', name=name)


@app.route('/submit', methods=['POST', 'GET'])
def process_query():
	# error = None
	# twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	# ACCESS_TOKEN = twitter.obtain_access_token()
	# twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
	data = []

	if request.method == 'POST':
		user_query = request.form["query"]
		user_lat = request.form["lat"]
		user_lon = request.form["lon"]
		user_rad = request.form["rad"]


		if (user_lat and user_lon):
			user_geo = "%s,%s,%smi" % (user_lat, user_lon, user_rad)
			data = queries.geo_query(query = user_query, geocode=user_geo, count=100)
			#data = queries.geo_query(geocode='34.07098,-118.4448,1mi', count=100)
		elif user_query:
			data = queries.single_query(query=user_query)


	if data:
		return render_template('results.html', results = data)
	else:
		return('no data')
if __name__ == '__main__':
	app.run(debug=True)