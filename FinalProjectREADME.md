#Analysis of World Development Indictors

##Introduction
The World Development Indicators from the World Bank contain over a thousand annual indicators of economic development from hundreds of countries around the world. I chose some of the indicators and countries to analysis, then get the figures to show plenty aspects, especially the analysis the development situation of China which is my mothercountry. Those output figures could state the situation clearly.


##Pre-exploration Steps:

In my FinalProject Folder there are three folders. There is a 'Analysis' folder which contanins 5 sub folders including folder analysis_1, analysis_2, analysis_3, analysis_4 and analysis_5. In each subfolder, there are one '.ipynb ' python nootebook file and a '.py' python file.
 
A folder named Data contains the dataset I used in this project. The main dataset I used are 'Indicadiors.csv' and 'Country.csv'. Others I used for looking up the indicator names and other information.

And the 'Output' folder contains 5 subfolders to palce the output figures for each analysis. Named like 'Analysis_1Output'.

##Getting Started:

To run this program you have to install the Python version at least Python 3. And I also recommend you to open with jupyter nootebook which has a better vision effect.

##Give examples:

To run the analysis_1. You should go to the 'Analysis' folder and open the folder 'analysis_1'. After double click the file,you could run the program in compiler which you have. Next run it.

###Analysis_1 

Analysis_1 shows the incomeGroup in Worldwide. In this analysis I use the data in Country.csv file. At first we read that file. And you could see 5 head rows of that file in the first ouput. And you can also checked the unique Region and country names. You will find some NaN vlaue in dataset.

It is better to drop the null value rows and duplicates value rows user will get a new dataframe names 'df_country'. And 'df' is data frame we extract for row 'Region' and 'Country'.  We could check the value countryName = China, and we will get information of China in this dataset.

The first out put figure is about to show how many countries in each incomegroup.

![alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis1_Output/A1_1.png)
![alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis1_Output/A1_2.png)
In this graph we could see the upper middle incomegroup has most of countries in. And China is also a upper middle incomegrop.

Then groupby these two cloumns and you will get like this:
Region                      IncomeGroup         
East Asia & Pacific         High income: OECD        4
                            High income: nonOECD     8
                            Low income               2
                            Lower middle income     12
                            Upper middle income     10
Europe & Central Asia       High income: OECD       24
                            High income: nonOECD    13
                            Lower middle income      8
                            Upper middle income     12
			    
And we add a column named "number_country" and make a new data frame names "result" and select the East Asia & Pacific Region part.

second output graph is :

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis1_Output/A1_2.png)
This is a Pie Chart of East Asia & Pacific Region IncomeGruop. That shows the percentage of each incomegroup in East Asia & Pacific Region.

And select the income value  = Low Income you can get a  dataframe:

                  Region	     IncomeGroup	    number_country
2	East Asia & Pacific	      Low income	       2
11	Latin America & Caribbean     Low income	       1
20	South Asia		      Low income               2
24	Sub-Saharan Africa	      Low income	       26
 
 And We can use this new dataset to get the Region of Low IncomeGruop Country Piecart
 
 [alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis1_Output/A1_3.png)
 
That shows the Sub-Saharan Africa get most low income group countries. And the percentage of each region.

Analysis_2:

This analysis is to see the Income(GDP) changes in 34years from 1970 to 2014.

Read the 'Indicators.csv' and in this file, the CountryName column contains some region's name that are not country's name.
So, create a list of region's name that we need to get rid of so that in next analysis we will get the correct result.
Get the querry 'NY.GNP.PCAP.CD' the year 1970  and sort the value by ascending.

The first output garph is to show the Lowest Average Income Countries i 1970:

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis2_Output/A2_1.png)

we can see the lowest GDP counteries in 1970, and China is in this list

And the same method but change the year to 2104 we would get the output figrue 2

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis2_Output/A2_2.png)

which shows the lowest GDP countries in 2014

Compare to this 2 graph, and get the same key in this 2 groups

Burundi,Central African Republic,Malawi,Mali,Togo  

are still the lowest gdp countries, but China is no longer in the list.

Next we could do the Highest Average Incomes Countries in year 1970 and 2014,get the years and querry and sort it,third figure is :

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis2_Output/A2_3.png)

use the same method but change the year, we get the 4th figure:

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis2_Output/A2_4.png)

These are the top 15 GDP countries, and get the key in 1970group and 2014 group, it shows 
Australia

Canada

Denmark

Kuwait

Luxembourg

Netherlands

Norway

Sweden

United States

 are  still th top 15 rich countries in the world.

Seeing these figrues and result we could know China is developingso fast and next we would see the income growth ratio between 
China and USA:

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis2_Output/A2_5.png)

In this graph we could see Income Ratio (2014 Income/1970 Income) of China is 61 and for USA is about 10.

That means China is developing so rapidly.

Aanlysis_3

As we know from that above, China is developing fast and I would like to see the engery use.
First the access to electricity, get the indicator EG.ELC.ACCS.RU.ZS names access to electricity in rural area and the 
indicator EG.ELC.ACCS.ZS means access to electricity in general area. From year 1990(because this data stars from this year) to 2014.

result shows thst:

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis3_Output/A3_1.png)

 That means China finally realize all country access to electricity not only urban area but also rural area .
 
 Next is to analysis the energy mix usage in the China.
 
 The indicators I use are:
 
EG.ELC.FOSL.ZS means Electricity production from oil, gas and coal sources (% of total)

EG.ELC.HYRO.ZS means Electricity production from hydroelectric sources (% of total)

EG.ELC.NUCL.ZS means Electricity production from Nuclear sources (% of total)

EG.ELC.RNWX.ZS means Electricity production from renewable sources, excluding hydroelectric (% of total)

And the graph shows that

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis3_Output/A3_2.png)

China is still rely on fossil fuels and hydroelectric sources. The reason why China also has a grate use of hydroelectric sources 

because we constructed a lots of hydroelectric power station and ofcourse the famous Three Gorges Hydropower Station. It is the world's largest power station in terms of installed capacity (22,500 MW). And we can also know from that figure that nuclear and renewable source are not so common use in China. So In China there are many envrioment problem.

Next, use the other indicators to anlysis the Fossil Fuel Mix in China (1970-2012) due to above analysis 

the result shows out:
[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis3_Output/A3_3.png)
Obviously, Coal source has been use most in China .

use the indicators of America,  it could do  the analysis that compare the Fossil Fuel Use Between China And USA

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis3_Output/A3_4.png)

It shows that China use further more Fossil Fuel than USA since 1975. And America reduce their fossil fuel year by year.

Analysis_4

This analysis ih all about population.

first choose the indicators EN.URB.LCTY.UR.ZS  that means Population in the largest city (% of urban population).

Use China , USA, India and Canada to do the comparsion.

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis4_Output/A4_2.png)

It shows China urban population percentage reduce form 1960 to 1980. Because more birth in rural area.

Next, the indicator EN.POP.DNST means Population density.

Try to compare the population density increasing between China and India from 1970 to 2014 that these two countries are largest population country.

 And the figure shows:
 
[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis4_Output/A4_1.png)

It shows India population density growth is fast then China.

And the third figure is compare the Number of infant deaths between USA, China and India

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis4_Output/A4_3.png)

Use the indicator : SH.DTH.IMRT means Number of infant deaths

shows that in China from 1970 to 1980 the number reduce actuely. And UAS is alway has very low nfant deaths number.

Analysis_5

Enviroment Problem

Use the indicator AG.LND.FRST.K2 ( Forest area (sq. km)) to compare the forest cover area between USA, China and India.

result:

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis5_Output/A5_1.png)

Forest cover area in China obviously increased in from 1990. 


Water productivity  analysis:

use indicator ER.GDP.FWTL.M3.KD ()

result:

[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis5_Output/A5_2.png)

Compare to Water productivity between China and India. The Water productivity in China increased actuely from 1995 to 2014.
While India is also increaed.


CO2 emissions sataement in the China
result:
[alt tag](https://github.com/zhangruiqi1/Python4DtaAnalysis/blob/master/FinalProject/Output/Analysis5_Output/A5_3.png)
use indicators EN.ATM.CO2E.KTE, EN.ATM.CO2E.GF.KT, EN.ATM.CO2E.LF.KT,EN.ATM.CO2E.SF.KT
Shows that emissions from solid fuel has come the most CO2 emissions for China.


Above is me Final Project ReadMe.







