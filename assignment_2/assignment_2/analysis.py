



# In

import argparse, datetime, os, json
import statistics
parser = argparse.ArgumentParser(description='Averge number')
parser.add_argument('--search_term', help='search term') 
parser.add_argument('--min_date', help= 'min day in yyyy-mm-dd') 
parser.add_argument('--max_date', help= 'max day in yyyy-mm-dd') 
args = parser.parse_args()
search_term = args.search_term
min_day = args.min_date
max_day = args.max_date
min_date =datetime.datetime.strptime(min_day, '%Y-%m-%d').date()
max_date =datetime.datetime.strptime(max_day, '%Y-%m-%d').date()
dif_days_int = (max_date-min_date).days

def add_days(days):
    r_date = min_date + datetime.timedelta(days =days)
    r_date_str = r_date.strftime('%Y-%m-%d')
    return r_date_str
                    
for i in range(0,dif_days_int +1):  
    parentPath = search_term +'/' + add_days(i)
    listdir = os.listdir(parentPath)
    list_friend_count = list()
    retweet_tweets = {}
    all_tweets = []
    for file in listdir:
        if (file.endswith('.json')):
            with open(parentPath + '/' + file) as f:
                content = json.load(f)
                tweets = content['statuses']
                i = 0
                for tweet in tweets:
                    friends_count = tweets[i]['user']['friends_count']
                    i += 1
                    list_friend_count.append(friends_count)
    avg_friends = int(statistics.mean(list_friend_count))
print('avg_friends:{0}'.format(avg_friends))



