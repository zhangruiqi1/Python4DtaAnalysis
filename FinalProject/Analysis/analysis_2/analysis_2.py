
# coding: utf-8

# In[13]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[27]:

indicators = pd.read_csv("/Users/ruiqizhang/Downloads/world-development-indicators//Indicators.csv")
#indicators.IndicatorName.unique()
indicators.CountryName.unique()
list = ['Arab World', 'Caribbean small states', 'Central Europe and the Baltics',
 'East Asia & Pacific (all income levels)',
 'East Asia & Pacific (developing only)', 'Euro area',
 'Europe & Central Asia (all income levels)',
 'Europe & Central Asia (developing only)', 'European Union',
 'Fragile and conflict affected situations',
 'Heavily indebted poor countries (HIPC)', 'High income',
 'High income: nonOECD', 'High income: OECD',
 'Latin America & Caribbean (all income levels)',
 'Latin America & Caribbean (developing only)',
 'Least developed countries: UN classification', 'Low & middle income',
 'Low income', 'Lower middle income',
 'Middle East & North Africa (all income levels)',
 'Middle East & North Africa (developing only)', 'Middle income',
 'North America' 'OECD members' ,'Other small states',
 'Pacific island small states', 'Small states', 'South Asia',
 'Sub-Saharan Africa (all income levels)',
 'Sub-Saharan Africa (developing only)' ,'Upper middle income' ,'World', 'North America', 'OECD members']

Lowest Average Income Countries
# In[70]:

lowestIC_2014 = indicators.query("IndicatorCode == 'NY.GNP.PCAP.CD' & CountryName != list & Year == 2014").sort_values(by = 'Value', ascending = True)[:15]
lowestIC_1970 = indicators.query("IndicatorCode == 'NY.GNP.PCAP.CD' & CountryName != list & Year == 1970").sort_values(by = 'Value', ascending = True)[:15]
#NY.GNP.PCAP.CD means GDP per capita (current US$)
Lchart1970 = sns.barplot(x = "Value", y = "CountryName", palette = "spring", data = lowestIC_1970)
plt.xlabel('Average Income (USD)', fontsize = 14)
plt.ylabel('Country',  fontsize=14)
plt.title('The 15 Countries with Lowest Average Income in 1970', fontsize = 14)
plt.show()


# In[69]:

#fig2 = plt.subplots()
Lchart2014 = sns.barplot(x = "Value", y = "CountryName", palette = "spring", data = lowestIC_2014)
plt.xlabel('Average Income (USD)', fontsize = 14)
plt.ylabel('Country', fontsize = 14)
plt.title('The 15 Countries with Lowest Average Income in 2014', fontsize = 14)
plt.show()


# In[40]:

for key,group in lowestIC_1970.groupby(['CountryName']):
    for key2, group2 in lowestIC_2014.groupby(['CountryName']):
        if key == key2:
            print (key)


# In[45]:

#for key,group in lowestIC_1970.groupby(['CountryName']):
   # for key2, group2 in lowestIC_2014.groupby(['CountryName']):
     #   if key != key2:
           #print (key)

China is no more a lowest income country
# In[37]:

China = indicators.loc[indicators['CountryName']==('China')]
China.head()

Highest Average Incomes Countries
# In[60]:

hightest_1970 = indicators.query("IndicatorCode == 'NY.GNP.PCAP.CD' & CountryName != list & Year == 1970").sort_values(by = 'Value')[-15:]
hightest_2014 = indicators.query("IndicatorCode == 'NY.GNP.PCAP.CD' & CountryName != list & Year == 2014").sort_values(by= 'Value')[-15:]

Hchart1970 = sns.barplot(x = "Value", y = "CountryName", palette = "summer", data = hightest_1970)
plt.xlabel('Average Income (USD)', fontsize = 14)
plt.ylabel('Country',  fontsize=14)
plt.title('The 15 Countries with Highest Average Income in 1970', fontsize = 14)
plt.show()


# In[67]:

Hchart2014 = sns.barplot(x = "Value", y = "CountryName", palette = "summer", data = hightest_2014)
plt.xlabel('Average Income ($)', fontsize = 14)
plt.ylabel('Country',  fontsize=14)
plt.title('The 15 Countries with Highest Average Income in 2014', fontsize = 14)
plt.show()


# In[74]:

for key,group in hightest_2014.groupby(['CountryName']):
    for key2, group2 in hightest_1970.groupby(['CountryName']):
        if key == key2:
            print (key)


# In[ ]:



