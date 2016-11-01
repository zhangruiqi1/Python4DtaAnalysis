
# coding: utf-8

# In[64]:

import json
import requests

q="https://api.stackexchange.com/2.0/questions?key=xYzIwB4x6ZaaMpb6JRFh*A((&page=1&pagesize=100&site=stackoverflow"
data=requests.get(q)
data=data.text
e=json.loads(data)
fp=open('top.json','w')
fp.write(json.dumps(e))
fp.close()
#print(e)


# In[ ]:

import json
import requests

q="https://api.stackexchange.com/2.2/questions?key=xYzIwB4x6ZaaMpb6JRFh*A((&page=1&pagesize=100&order=desc&sort=activity&tagged=python;pandas&site=stackoverflow"
data=requests.get(q)
data=data.text
m=json.loads(data)
fp=open('pythonpandas.json','w')
fp.write(json.dumps(m))
fp.close()
#print(m)


# In[65]:

import json
import requests

q="https://api.stackexchange.com/2.2/badges?key=xYzIwB4x6ZaaMpb6JRFh*A((&page=1&pagesize=100&order=desc&sort=rank&site=stackoverflow"
data=requests.get(q)
data=data.text
l=json.loads(data)
fp=open('badges.json','w')
fp.write(json.dumps(l))
fp.close()
#print(l)

/2.2/badges?page=1&pagesize=100&order=desc&sort=rank&site=stackoverflow
/2.2/questions?page=1&pagesize=100&order=desc&sort=activity&site=stackoverflow
/2.2/answers?page=1&pagesize=100&order=desc&sort=activity&site=stackoverflow&filter=!-.7zMl7nRqbD
# In[66]:

import json
import requests

q="https://api.stackexchange.com/2.2/questions?key=xYzIwB4x6ZaaMpb6JRFh*A((&page=6&pagesize=100&order=desc&sort=activity&site=stackoverflow"
data=requests.get(q)
data=data.text
h=json.loads(data)
fp=open('que5.json','w')
fp.write(json.dumps(h))
fp.close()
#print(h)


# In[67]:

import json
import requests

q="https://api.stackexchange.com/2.2/answers?key=xYzIwB4x6ZaaMpb6JRFh*A((&page=6&pagesize=100&order=desc&sort=activity&site=stackoverflow&filter=!-.7zMl7nRqbD"
data=requests.get(q)
data=data.text
h=json.loads(data)
fp=open('devotecount5.json','w')
fp.write(json.dumps(h))
fp.close()
#print(h)


# In[ ]:



