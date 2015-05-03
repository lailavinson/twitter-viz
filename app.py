from twython import Twython

APP_KEY = "Qn4Nx6C9LtoAlKtYLtoNQX2uY"
APP_SECRET = "mFk56Ec74tSW74Dp8uQqmyxMHKVeMAgQU8cLjRFqV3Ro87cSiN"

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
twitter.search(q='python')
