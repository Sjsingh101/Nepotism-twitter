import tweepy
import pandas as pd
import csv

consumer_key = 'yhF5NebEvzpMFYsiWhCt83qBh'
consumer_secret = '7R0WZe2RJtribXeslG6mDCMlMA4gudyf2yDGZXgvB77qtP4cSR'
access_token = '1033426617261903877-W9zG51kIzB3GVhoco2zwPIdl6Qt2NB'
access_token_secret = 'piiX2kZsZBnG5CtMvcczwI1sGTW4a5JFipZi6okyMJX43'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# creation of the actual interface, using authentication
api = tweepy.API(auth)

api = tweepy.API(auth,wait_on_rate_limit = True)

df = pd.DataFrame()
msgs = []
msg =[]

for tweet in tweepy.Cursor(api.search, q='#NisargaCyclone', count=100).items(4000):
    msg = [tweet.text, tweet.source, tweet.source_url] 
    msg = tuple(msg)                    
    msgs.append(msg)

df = pd.DataFrame(msgs,columns=['text', 'source', 'url'])

df.head()

df.to_csv('tweets.csv')