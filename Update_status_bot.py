#!/usr/bin/env python3
import tweetpy1

#import twitter apps configaration file from config.py file
from config import *

#Authentication using keys & accesstoken
auth = tweetpy1.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweetpy1.API(auth)

api.update_status(status="This is a sample tweet using Tweetpy1 with python")