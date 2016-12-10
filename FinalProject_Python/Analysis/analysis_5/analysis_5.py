
# coding: utf-8

# In[22]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import fill_between


# In[3]:

indicators = pd.read_csv("/Users/ruiqizhang/Downloads/world-development-indicators//Indicators.csv")
#indicators.IndicatorName.unique()
#indicators.CountryName.unique()


# In[ ]:

#ER.H2O.INTR.PC means  Renewable internal freshwater resources per capita (cubic meters)
#ER.GDP.FWTL.M3.KD Water productivity, total (constant 2005 US$ GDP per cubic meter of total freshwater withdrawal)


# In[20]:

#AG.LND.FRST.K2 means Forest area (sq. km))
fchina = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='AG.LND.FRST.K2')]
fusa =  indicators[(indicators.CountryName=='United States')&(indicators.IndicatorCode=='AG.LND.FRST.K2')]
findia = indicators[(indicators.CountryName=='India')&(indicators.IndicatorCode=='AG.LND.FRST.K2')]
fig = plt.figure()
plt.plot(fchina.Year,fchina.Value,'o-',color='g',label='China')
plt.plot(fusa.Year,fusa.Value,'o-',color='cyan',label='USA')
plt.plot(findia.Year,findia.Value,'o-',color='greenyellow',label='India')
plt.xlabel('Years')
plt.ylabel('forest area in sq. km')
plt.title('forest Area comparison ')
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)
plt.savefig('A5_1.png')


# In[19]:

wchina = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='ER.GDP.FWTL.M3.KD')]
windia = indicators[(indicators.CountryName=='India')&(indicators.IndicatorCode=='ER.GDP.FWTL.M3.KD')]
fig = plt.figure()
plt.plot(wchina.Year,wchina.Value,'o-',color='blue',label='China')
plt.plot(windia.Year,windia.Value,'o-',color='pink',label='India')
plt.xlabel('Years')
plt.ylabel('cubic meter')
plt.title('Water productivity  ')
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)
plt.savefig('A5_2.png')


# In[31]:

df_elec_emi = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EN.ATM.CO2E.KT')]
df_elec_gf = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EN.ATM.CO2E.GF.KT')]
df_elec_lf = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EN.ATM.CO2E.LF.KT')]
df_elec_sf = indicators[(indicators.CountryName=='China')&(indicators.IndicatorCode=='EN.ATM.CO2E.SF.KT')]

fig = plt.figure()

plt.plot(df_elec_emi.Year,df_elec_emi.Value,label='C0$_2$ emissions',color='yellow')
plt.plot(df_elec_lf.Year,df_elec_lf.Value,label='C0$_2$ emissions from liquid fuel',color='lightcoral')
plt.plot(df_elec_sf.Year,df_elec_sf.Value,label='C0$_2$ emissions from solid fuel',color='lime')
plt.plot(df_elec_gf.Year,df_elec_gf.Value,label='C0$_2$ emissions from gaseous fuel',color='pink')

fill_between(df_elec_emi.Year,df_elec_emi.Value,0,alpha=0.5,color='yellow')
fill_between(df_elec_lf.Year,df_elec_lf.Value,0,alpha=0.5,color='lightcoral')
fill_between(df_elec_sf.Year,df_elec_sf.Value,0,alpha=0.5,color='orange')
fill_between(df_elec_gf.Year,df_elec_gf.Value,0,alpha=0.5,color='pink')

plt.legend(loc=2, borderaxespad=1.)
plt.xlabel('Years',  fontsize=14)
plt.ylabel('kt (kilotons)',  fontsize=14)
plt.title('CO2 emissions sataement in the China', fontsize=18)
plt.savefig('A5_3.png')




# In[ ]:



