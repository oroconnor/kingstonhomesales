#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:32:52 2020

@author: owenoconnor
"""



import pandas as pd
import matplotlib.pyplot as plt

#read the realtor.com data into a pandas dataframe
df = pd.read_csv("/Users/owenoconnor/Documents/scripts/realtor/kingston update/RDC_Inventory_Hotness_Metrics_Zip_History_OCT20.csv")

#convert the string dates into datetime objects, and then setting that column as the index for the dataframe.
df["date_dt"]  = pd.to_datetime(df["month_date_yyyymm"], format = "%Y%m", errors = "coerce") 
df.index = df["date_dt"]


#%%
kingston = df[df["postal_code"] == 12401]#extract the data just for Kingston, NY
#with just a few of the columns that we're interested in looking at
kingston_subset = kingston[['hotness_score','median_days_on_market','median_listing_price']] 
kingston_subset["month"]=kingston_subset.index.month #adds a month column that we can use to sort by





#%%
#pull out a subset that holds the info for just September from the years available
kingston_september = kingston_subset[kingston_subset.index.month == 9]

#create the figure showing the July info (across 4 years) for Median Listing Price and Median Days on Market
fig = plt.figure()
fig.set_size_inches([6,6])
axes1 = fig.add_subplot(2,1,1)
axes2 = fig.add_subplot(2,1,2)
axes1.plot(kingston_september.index,kingston_september['median_listing_price'], linestyle = "--", marker = "o", color = "red")
axes2.plot(kingston_september.index, kingston_september['median_days_on_market'], linestyle = "--", marker = "o", )
axes1.set_title("Median Listing Price - September, 2017-2020")
axes1.set_ylabel("Listing Price $")
axes2.set_title("Median Days on Market - September, 2017-2020")
axes2.set_ylabel("Days")
plt.xticks(kingston_september.index,rotation = 90)
plt.suptitle("Kingston NY - Home Sales Data", y = 1.02,fontsize =16)
plt.figtext(0,-.02, "Data source: https://www.realtor.com/research/data/ ")
fig.autofmt_xdate()
fig.tight_layout()

fig.savefig("10_20kingstondata_1.jpg", bbox_inches = "tight")



#%%

#organize data by year and just take the info for Jan-Sep
kingston_2017start = kingston_subset["2017-09":"2017-01"]
kingston_2018start = kingston_subset["2018-09":"2018-01"]
kingston_2019start = kingston_subset["2019-09":"2019-01"]
kingston_2020start = kingston_subset["2020-09":"2020-01"]

#plot the Median Days on Market for these four years, Jan-Sept
fig, ax = plt.subplots()
ax.plot(kingston_2017start["month"],kingston_2017start["median_days_on_market"], linestyle = "--", label = "2017")
ax.plot(kingston_2018start["month"],kingston_2018start["median_days_on_market"], linestyle = "--", label = "2018")
ax.plot(kingston_2019start["month"],kingston_2019start["median_days_on_market"], linestyle = "--", label = "2019")
ax.plot(kingston_2020start["month"],kingston_2020start["median_days_on_market"], label = "2020")
ax.legend()
ax.set_ylabel("Median Days on the Market")
ax.set_xlabel("Month")
plt.suptitle("Days on the Market - Jan-Sept of Past Four Years")
plt.figtext(0,-.05, "Data source: https://www.realtor.com/research/data/  , market hotness index")
fig.savefig("10_20kingstondata_2.jpg", bbox_inches = "tight")

#%%
#now plotting the Median Days on Market for all the months of the year
kingston_2017 = kingston_subset["2017"]
kingston_2018 = kingston_subset["2018"]
kingston_2019 = kingston_subset["2019"]
kingston_2020 = kingston_subset["2020"]

fig, ax = plt.subplots()
ax.plot(kingston_2017["month"],kingston_2017["median_days_on_market"], linestyle = "--", label = "2017")
ax.plot(kingston_2018["month"],kingston_2018["median_days_on_market"], linestyle = "--", label = "2018")
ax.plot(kingston_2019["month"],kingston_2019["median_days_on_market"], linestyle = "--", label = "2019")
ax.plot(kingston_2020["month"],kingston_2020["median_days_on_market"], label = "2020")
ax.legend()
ax.set_ylabel("Median Days on the Market")
ax.set_xlabel("Month")
plt.suptitle("Days on the Market - Past Four Years")
plt.figtext(0,-.05, "Data source: https://www.realtor.com/research/data/")
fig.savefig("10_20kingstondata_3.jpg", bbox_inches = "tight")

#%%
fig, ax = plt.subplots()
ax.plot(kingston_subset.index,kingston_subset['median_listing_price'])
ax.axhline(y = 276000, color = "g", linestyle = "--", label = "$276,000")
ax.axhline(y = 233896, color = "r", linestyle = "--", label = "$233,986")
ax.set_ylabel('Median Listing Price')
ax.set_xlabel("Year and Month")
ax.legend()
plt.suptitle("Median Listing Price - Past Four Years")
plt.figtext(0,-.05, "Data source: https://www.realtor.com/research/data/")
fig.autofmt_xdate()
fig.savefig("10_20kingstondata_4.jpg", bbox_inches = "tight")

