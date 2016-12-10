
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:

indicators = pd.read_csv("/Users/ruiqizhang/Downloads/world-development-indicators//Indicators.csv")
#indicators.IndicatorName.unique()
#indicators.CountryName.unique()


# In[43]:

#code EN.URB.LCTY.UR.ZS means Population in the largest city (% of urban population)
China_population_largest_city = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EN.URB.LCTY.UR.ZS')]
USA_population_largest_city = indicators[(indicators.CountryName=='United States')&(indicators.IndicatorCode=='EN.URB.LCTY.UR.ZS')]
India_population_largest_city = indicators[(indicators.CountryName=='India')&(indicators.IndicatorCode=='EN.URB.LCTY.UR.ZS')]
Canada_population_largest_city = indicators[(indicators.CountryName=='Canada')&(indicators.IndicatorCode=='EN.URB.LCTY.UR.ZS')]
fig = plt.figure()
plt.plot(China_population_largest_city.Year,China_population_largest_city.Value,color='pink',label='China')
plt.plot(USA_population_largest_city.Year,USA_population_largest_city.Value, color='cyan',label='USA')
plt.plot(India_population_largest_city.Year,India_population_largest_city.Value, color='tomato',label='Inida')
plt.plot(Canada_population_largest_city.Year,Canada_population_largest_city.Value, color='yellowgreen',label='Canada')
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)
plt.xlabel('Years',  fontsize=14)
plt.ylabel('% of Population',  fontsize=14)
plt.title('Percentage of urban population', fontsize=14)
#plt.show()
plt.savefig('A4_2.png')


# In[40]:

#EN.POP.DNST means Population density 

PD1970 = indicators.query("IndicatorCode == 'EN.POP.DNST' & Year == 1970 & CountryName == [ 'China','India']")
PD2014 =indicators.query("IndicatorCode == 'EN.POP.DNST' & Year == 2014 & CountryName == [ 'China', 'India']")

a = pd.Series(PD2014['Value'].reset_index(drop = True))
b = pd.Series(PD1970 ['Value'].reset_index(drop = True))
ratio = a/b

pd_ratio = sns.barplot(x = ['China', 'India'], y = ratio, order = ['China','India' ])
plt.title('Comparsion Population density Increasing Between China And India ', fontsize = 14)
plt.xlabel('Country', fontsize = 10)
plt.ylabel('Population density Ratio (2014 debsity/1970 density)', fontsize = 10)

         
plt.savefig('A4_1.png')


# In[ ]:

fig12, axs12 = plt.subplots(figsize = [15,8])
labels_cross3pt2 = []
for key, group in document.query("IndicatorCode == 'NY.GNP.PCAP.CD' & CountryName == ['China', 'Malawi', 'Luxembourg', 'United States']").groupby(['CountryName']):
    axs12 = group.plot(ax = axs12, kind = "line", x = "Year", y = "Value", title = "Comparing average income- China vs Malawi vs Luxembourg vs US")
    labels_cross3pt2.append(key)

lines,_ = axs12.get_legend_handles_labels()
axs12.legend(lines, labels_cross3pt2, loc = 'best')


# In[54]:

#SH.DTH.IMRT means Number of infant deaths
China = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='SH.DTH.IMRT')]
India = indicators[(indicators.CountryName=='India')&(indicators.IndicatorCode=='SH.DTH.IMRT')]
USA = indicators[(indicators.CountryName=='United States')&(indicators.IndicatorCode=='SH.DTH.IMRT')]
#Canada = indicators[(indicators.CountryName=='Canana')&(indicators.IndicatorCode=='SH.DTH.IMRT')]
fig = plt.figure()
plt.plot(China.Year,China.Value,color='orange',label='China')
plt.plot(India.Year,India.Value,color='blue',label='India')
plt.plot(USA.Year,USA.Value,color='green',label='USA')
#plt.plot(Canada.Year,Canada.Value,color='red',label='Canada')
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)
plt.xlabel('Years',  fontsize=14)
plt.ylabel('Number of Infant death',  fontsize=14)
plt.title('Number of Infant death from 1970 to 2014', fontsize=14)
plt.show()
plt.savefig('A4_3.png')


# In[ ]:



