
# coding: utf-8

# In[87]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import glob


# In[8]:

country = pd.read_csv('/Users/ruiqizhang/Downloads/world-development-indicators/Country.csv')
country.head()


# In[13]:

#clear the data
country.IncomeGroup.unique()


# In[21]:

country.Region.unique()


# In[15]:

country_array =  country[['ShortName','CountryCode']].drop_duplicates().values


# In[55]:

df_country = country[pd.notnull(country['Region'])]


# In[56]:

df_country.Region.unique()
df_country.IncomeGroup.unique()


# In[149]:

China = df_country.loc[df_country['ShortName']==('China')]
China


# In[70]:

df=df_country[['Region','IncomeGroup']]
df.head()


# In[126]:

import pandas as pd
import matplotlib.pyplot as plt
df.IncomeGroup.value_counts().plot(kind='barh')
plt.title('Worldwide IncomeGruop Analysis')
plt.xlabel('Number of Country')


# In[72]:

df.groupby(["Region", "IncomeGroup"]).size()


# In[134]:

result = df.groupby(["Region", "IncomeGroup"]).size().reset_index(name="number_country")
result


# In[114]:

Ep = result.loc[result['Region']==('East Asia & Pacific')]
Ep


# In[203]:

from matplotlib.pyplot import pie, axis, show
plt.figure(figsize=plt.figaspect(1))
labels = ['High income: OECD', 'High income: nonOECD', 'Low income', 'Lower middle income','Upper middle income']
values = [4, 8, 2, 12,10]
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','pink']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90,)
plt.pie(values, autopct=make_autopct(values),colors=colors)
plt.legend(patches, labels, loc="best")
plt.tight_layout()
plt.axis('equal')
plt.title('Pie Chart of East Asia & Pacific Region IncomeGruop Analsis ')
plt.show()


# In[130]:

low = result.loc[result['IncomeGroup']==('Low income')]
low


# In[183]:

import matplotlib.pyplot as plt

plt.figure(figsize=plt.figaspect(1))
values = [2, 2, 2, 26] 
labels = ['East Asia & Pacific', 'Latin America & Caribbean', 'South Asia', 'Sub-Saharan Africa'] 
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
colors = ['yellowgreen', 'gold', 'lightskyblue', 'pink']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.pie(values, labels=labels, autopct=make_autopct(values),colors=colors)
plt.legend(patches, labels, loc="upper left")
plt.axis('equal')
plt.tight_layout()
plt.title('Region of Low IncomeGruop Country Analsis ')
plt.show()


# In[ ]:



