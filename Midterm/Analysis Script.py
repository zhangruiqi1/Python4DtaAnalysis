
# coding: utf-8

# In[43]:

import json
b = json.loads(open("/Users/ruiqizhang/DAPassignment/Midterm/tag/pythonpandas.json").read())
result = {}
for i in b['items']:
    userid= i["owner"]["user_id"]
    if userid not in result:
        result[i["owner"]["user_id"]  ] = []
    result[userid].append( i)
#use user id to get usr profile
weight_dict = {}    
for usr_id in result.keys():
    fp = open('/Users/ruiqizhang/DAPassignment/Midterm/1/%s'%(usr_id),'r')
    b  = json.loads(fp.read()) 
    #b = json.loads(data)
    #print(b)
    badge_counts = b['items'][0]['badge_counts']
    weight_dict[usr_id] = badge_counts['gold']*100 + badge_counts['silver']*10 + badge_counts['bronze']
#show top usrid 's questions
for usr_id,value in sorted(weight_dict.items(),key = lambda x:x[1],reverse = True)[:1]:
    for que in result[usr_id]:
        print('top questions according to the weightage:')
        print(que['title'])

   
         


# In[ ]:

Analysis 2


# In[48]:

import json 
result = json.loads(open("/Users/ruiqizhang/DAPassignment/Midterm/tag/pythonpandas.json").read())
tag_dict = {}  
# get all the tags
for v in result['items']:
    for tag in v[ "tags"]:
        if tag not in tag_dict:
            tag_dict[tag] = set()
        tag_dict[tag].add((v['owner']['user_id'], v['owner']['display_name'], v['owner']['link']))
#for usr_id,value in result.items():
        #for tag in value[ "tags"]:
            #if tag not in tag_dict:
                 #tag_dict[tag] = set()
             #tag_dict[tag].add((usr_id, value['owner']['display_name'], value['owner']['link']))
            
fp = open('analyze2.txt','w')
for key,value in tag_dict.items():
    fp.write("%s %s\n"%(key,value ) )
fp.close()
    #find the topic python  user
for i in tag_dict['python']:
    print(' user who have reputation in tag python:')
    print(i)
    break
    

Analysis 3
# In[15]:

import json 
b = json.loads(open("/Users/ruiqizhang/DAPassignment/Midterm/tag/pythonpandas.json").read())
result = {}
for i in b['items']:
    userid= i["owner"]["user_id"]
    if userid not in result:
        result[i["owner"]["user_id"]  ] = []
    result[userid].append( i)
#use user id to get usr profile
badge_list = {'gold':0,'silver':0,'bronze':0}   
for usr_id in result.keys():
    fp = open('./1/%s'%(usr_id),'r')
    b  = json.loads(fp.read()) 
    badge_counts = b['items'][0]['badge_counts']
    badge_list['gold'] += 0   if badge_counts['gold'] == 0 else 1
    badge_list['silver'] +=0   if  badge_counts['silver'] == 0 else 1
    badge_list['bronze'] += 0   if badge_counts['bronze'] == 0 else 1
print("Each badge type have these usres ",  sorted(badge_list.items(),key = lambda x: x[1],reverse = True ))


# In[ ]:

Analysis 4


# In[50]:

import json 
import csv
result = json.loads(open("/Users/ruiqizhang/DAPassignment/Midterm/que.json").read())
que_dict = {}
for v in result['items']:
    if v['title'] not in que_dict:
        que_dict[v['title']] = set()
    que_dict[v['title']] =  que_dict[v['title']] | set( v['tags'])
#For each of the question that is asked, find out the tags attached to it.
print('Tags attached to for each of the question: ')
print(que_dict)

#find how many time
que_dict2 = {}
for v in result['items']:
    if v['title'] not in que_dict2:
        que_dict2[v['title']] = 0
    que_dict2[v['title']] +=  v['answer_count']
#For each tag, calculate the number of question asked and how many times it has been answered.
tag_dict = {}
for key,value in que_dict.items():
    for t in value:
        if t not in tag_dict:
            tag_dict[t] = [0,0]
        tag_dict[t][0] += 1
        tag_dict[t][1] += que_dict2[key]
print(' For each tag, number of question asked,times ithas been answered:')
print(tag_dict)    #the first element in the list is the the number of question asked  ,the second element is the how many times it has been answered.


# In[39]:

import json
result = json.loads(open("/Users/ruiqizhang/DAPassignment/Midterm/devotecount/devotecount.json").read())
usrid_devote_dict = {}
#get all the ur message
for v in result['items']:
    if v['owner']['user_id'] not in usrid_devote_dict:
        usrid_devote_dict[ v['owner']['user_id'] ] = [v['owner']['display_name'], 0]
#get each usr 's disvote counts
for v in result['items']:
    usrid_devote_dict[ v['owner']['user_id'] ][1] += v['down_vote_count']
#Print the usrid_devote_dict.
#print(usrid_devote_dict)
#sort the dict to get the max counts of disvote

sort_data = sorted(usrid_devote_dict.items() , key = lambda x: x[1][1],reverse = True)

#print(sort_data)
the_max_count = sort_data[0][1][1]
#find the max count's user name
print("the user whose questions have been downvoted the most: \n\nUser name:    Counts")
for data in sort_data:
    
    if data[1][1] == the_max_count:
        print(data[1][0] ,":",data[1][1])

For Analysis1 use userid to send request to get profile
# In[ ]:

import json
b = json.loads(open("pythonpandas.json").read())
result = {}
for i in b['items']:
    userid= i["owner"]["user_id"]
    if userid not in result:
        result[i["owner"]["user_id"]  ] = []
    result[userid].append( i)
for usr_id in result.keys():
    q =  "https://api.stackexchange.com/2.2/users/%s?order=desc&sort=reputation&site=stackoverflow"%(usr_id)
    data = requests.get(q)
    data = data.text
    fp = open('./1/%s'%(usr_id),'w')
    fp.write(json.dumps( json.loads(data)) )
    fp.close()

Analysis 5 (save data as csv)
# In[35]:

import json
import os
import csv


path = r"./devotecount"

filse = []
current_files = os.listdir(path)
for file_name in current_files:
    if '.json' in file_name:
        full_file_name = os.path.join(path, file_name)
        filse.append(full_file_name)



for f in filse:


    result = json.loads(open(f).read())
    usrid_devote_dict = {}
    #get all the usr message
    for v in result['items']:
        if v['owner']['user_id'] not in usrid_devote_dict:
            usrid_devote_dict[ v['owner']['user_id'] ] = [v['owner']['display_name'].encode('gbk','ignore').decode('gbk'), 0]

    #get each usr 's disvote counts
    for v in result['items']:

        usrid_devote_dict[ v['owner']['user_id'] ][1] += v['down_vote_count']

    #Print the usrid_devote_dict.
    #print(usrid_devote_dict)
       
        
    #sort the dict to get the max counts of disvote

sort_data = sorted(usrid_devote_dict.items() , key = lambda x: x[1][1],reverse = True)

#print(sort_data)
csvfile = open('analyze_5.csv', 'w')
writer = csv.writer(csvfile)

the_max_count = sort_data[0][1][1]
    #find the max count's user name
print("the user whose questions have been downvoted the most: \n\nUser name:    Counts")
for data in sort_data:
        
    if data[1][1] == the_max_count:
        print(data[1][0] ,":",data[1][1])
   
writer.writerows(sort_data)
csvfile.close()


Analysis 4(save output as csv)
# In[52]:

import json
import os
import csv

path = r"./que"


filse = []
current_files = os.listdir(path)
for file_name in current_files:
    if '.json' in file_name:
        full_file_name = os.path.join(path, file_name)
        filse.append(full_file_name)
        
for f in filse:


    result = json.loads(open(f).read())
    que_dict = {}
    for v in result['items']:
        if v['title'] not in que_dict:
            que_dict[v['title']] = set()
        que_dict[v['title']] =  que_dict[v['title']] | set( v['tags'])

    #For each of the question that is asked, find out the tags attached to it.
    #print(que_dict)
            
    #find how many time
    que_dict2 = {}
    for v in result['items']:
        if v['title'] not in que_dict2:
            que_dict2[v['title']] = 0
        que_dict2[v['title']] +=  v['answer_count']

#For each tag, calculate the number of question asked and how many times it has been answered.

tag_dict = {}
for key,value in que_dict.items():

    for t in value:
        if t not in tag_dict:
            tag_dict[t] = [0,0]
        tag_dict[t][0] += 1
        tag_dict[t][1] += que_dict2[key]


tag_list = [(  key,value)    for key,value in tag_dict.items()  ]

csvfile = open('analyze_4.csv', 'w')
writer = csv.writer(csvfile)

writer.writerows(tag_list)
csvfile.close()
print(' For each tag, number of question asked,times ithas been answered:')       
print(tag_dict)    #the first element in the list is the the number of question asked  ,the second element is the how many times it has been answered.



# In[ ]:




# In[ ]:



