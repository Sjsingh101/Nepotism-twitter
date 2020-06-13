import tweepy
import pandas as pd
import csv

consumer_key = 'XXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXX'
 
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
