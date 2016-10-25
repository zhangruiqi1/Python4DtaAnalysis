
# coding: utf-8

# In[22]:

import oauth2 as oauth
import json

CONSUMER_KEY = "FMu8rK3UtpYtZKNSmmsFhCHMy"
CONSUMER_SECRET = "EkhiUmrhfFxXyRIX3PJZxwuiAQOQaboBWA1CmZdoesw1mbNenP"
ACCESS_KEY = "4335237629-d2T92cEIqmLs3QSvDsE7U6lHRMFFMZOSvxpLcJp"
ACCESS_SECRET = "PzR7pAh3EJtlZU8C5xlCRf6TmHsPh4CjjUnSXyLegQXLk"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=%Election2016until:2016-10-23&count=100"
response, data = client.request(timeline_endpoint)
tweets = json.loads(data.decode('utf-8'))
#type(tweets) 
for tweet in tweets:
#print (tweet['text'])
    print (data.decode('utf-8'))
#fp=open('Election2016h.json','w')
#fp.write(json.dumps(data.decode('utf-8')))
#fp.close()




# In[1]:

import oauth2 as oauth
import json

CONSUMER_KEY = "FMu8rK3UtpYtZKNSmmsFhCHMy"
CONSUMER_SECRET = "EkhiUmrhfFxXyRIX3PJZxwuiAQOQaboBWA1CmZdoesw1mbNenP"
ACCESS_KEY = "4335237629-d2T92cEIqmLs3QSvDsE7U6lHRMFFMZOSvxpLcJp"
ACCESS_SECRET = "PzR7pAh3EJtlZU8C5xlCRf6TmHsPh4CjjUnSXyLegQXLk"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=%Election2016since:2016-10-15"
response, data = client.request(timeline_endpoint)
tweets = json.loads(data.decode('utf-8'))
for tweet in tweets:
#print (tweet['text'])
    print (data.decode('utf-8'))
#fp=open('Eectionl1015q.json','w')
#fp.write(json.dumps(data.decode()))
#fp.close()

