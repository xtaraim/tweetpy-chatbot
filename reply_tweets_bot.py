import tweetpy1

consumer_key = 'your consumer_key'

consumer_secret = 'your consumer_secret'

access_token = 'your acess_token'

acess_token_secret = 'your acess_token_secret'

auth = tweetpy1.OAuthHandler(consumer_key, consumer_secret)

auth.set_acess_token(access_token, access_token_secret)

api = tweetpy1.API(auth)


twt = api.search(q="Hello World")

#list of strings that we want to check from tweets
txt = ['Hello world!',
    'Hello World!',
    'Hello World!!!',
    'Hello world!!!',
    'Hello, world!',
    'Hello, World!']

#Its can take many time
for st in twt:
	for s in txt:
		if s == st.text:
			usr = st.user.screen_name
			msg = ("@%s Hello!" %(usr))
			st = api.update_status(msg, st.id)