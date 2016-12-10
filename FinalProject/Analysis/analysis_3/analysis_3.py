
# coding: utf-8

# In[84]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import fill_between


# In[2]:

indicators = pd.read_csv("/Users/ruiqizhang/Downloads/world-development-indicators//Indicators.csv")
#indicators.IndicatorName.unique()
indicators.CountryName.unique()


# In[78]:

rural = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.ACCS.RU.ZS')]
general = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.ACCS.ZS')]

fig = plt.figure()
plt.ylim([90,110])
plt.plot(rural.Year,rural.Value,'o-',label='Rural',color='lightgreen')
plt.plot(general.Year,general.Value,'o-',label='General',color='gold')
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)
plt.xlabel('Years',  fontsize=14)
plt.ylabel('% of Population',  fontsize=14)

plt.title('Access to Electricity', fontsize=14)
#plt.show()
plt.savefig('A3_1.png')


# In[55]:

#EG.ELC.FOSL.ZS means Electricity production from oil, gas and coal sources (% of total)
#EG.ELC.HYRO.ZS means Electricity production from hydroelectric sources (% of total)
#EG.ELC.NUCL.ZS means Electricity production from hydroelectric sources (% of total)
#EG.ELC.RNWX.ZS means Electricity production from renewable sources, excluding hydroelectric (% of total)
elec_fosl = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.FOSL.ZS')]
elec_hydro = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.HYRO.ZS')]
elec_nucl = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.NUCL.ZS')]
elec_rnwx = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.RNWX.ZS')]


fig = plt.figure()

plt.plot(elec_fosl.Year,elec_fosl.Value,label='Fossil Fuels',color='dimgray')
plt.plot(elec_hydro.Year,elec_hydro.Value,label='Hydroelectric',color='lightcyan')
plt.plot(elec_nucl.Year,elec_nucl.Value,label='Nuclear',color='lightpink')
plt.plot(elec_rnwx.Year,elec_rnwx.Value,label='Renewable',color='palegreen')


fill_between(elec_fosl.Year,elec_fosl.Value,0,alpha=0.3,color='dimgray')
fill_between(elec_hydro.Year,elec_hydro.Value,0,alpha=0.5,color='lightcyan')
fill_between(elec_nucl.Year,elec_nucl.Value,0,alpha=0.5,color='lightpink')
fill_between(elec_rnwx.Year,elec_rnwx.Value,0,alpha=1,color='palegreen')


plt.legend(loc="upper right", borderaxespad=1.)
plt.xlabel('Years',  fontsize=14)
plt.ylabel('% of Total Energy Produce',  fontsize=14)
plt.title('Energy Mix in the China (1970-2012)', fontsize=18,)
plt.savefig('A3_2.png')


# In[68]:

elec_ngas = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.NGAS.ZS')]
elec_coal = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.COAL.ZS')]
elec_petr = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.PETR.ZS')]

fig = plt.figure()

plt.plot(elec_ngas.Year,elec_ngas.Value,label='Natural Gas',color='gold')
plt.plot(elec_coal.Year,elec_coal.Value,label='Coal',color='mediumpurple')
plt.plot(elec_petr.Year,elec_petr.Value,label='Petroleum',color='aqua')

fill_between(elec_petr.Year,elec_petr.Value,0,alpha=0.3,color='aqua')
fill_between(elec_coal.Year,elec_coal.Value,0,alpha=0.5,color='mediumpurple')
fill_between(elec_ngas.Year,elec_ngas.Value,0,alpha=1,color='gold')


plt.legend(loc="best", borderaxespad=1.)
plt.xlabel('Years',  fontsize=14)
plt.ylabel('Percentage of Total Energy Produce',  fontsize=14)
plt.title('Fossil Fuel Mix in China (1970-2012)', fontsize=18)
plt.savefig('A3_3.png')


# In[94]:

df_USA_elec_pop = indicators[(indicators.CountryName=='United States')&(indicators.IndicatorCode=='EG.ELC.FOSL.ZS')]
elec_fosl = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EG.ELC.FOSL.ZS')]
fig = plt.figure()

plt.plot(df_USA_elec_pop.Year,df_USA_elec_pop.Value,label='USA',color='peru')
plt.plot(elec_fosl.Year,elec_fosl.Value,label='China',color='dimgray')

plt.legend(loc="best", borderaxespad=1.)
plt.xlabel('Years',  fontsize=14)
plt.ylabel('% of Energy Production',  fontsize=14)
plt.title('Fossil Fuel Use for SEA Countries', fontsize=16)

plt.xlim([1970,2020])  
plt.savefig('A3_4.png')


# In[ ]:



