# -*- coding: utf-8 -*-
"""
Get Option Volume By Expiration

@author: Adam Getbags
"""

#import modules
from yahoo_fin import options as op
import time as t
import pandas as pd
import os
from datetime import datetime, date
import requests

#list for data 
expirationDate = []
daysToExpiration = []
totalVolumeByExpiration = []

#input ticker
ticker = 'PLTR'

#date information
today = date.today()
todaysDate = datetime(today.year, today.month, today.day)

#get expiration dates
expirationDates = op.get_expiration_dates(ticker)

#for loop per expiration cycle
for i in range(0, len(expirationDates)):

    expDate = datetime.strptime(expirationDates[i], '%B %d, %Y')    

    #get DTE
    DTE = (expDate - todaysDate).days
    
    #chain data
    chainData = op.get_options_chain(ticker, date = expirationDates[i])
    
    #to numeric data type
    chainData['calls']['Volume'] = pd.to_numeric(
        chainData['calls']['Volume'], errors = 'coerce')
    
    chainData['puts']['Volume'] = pd.to_numeric(
        chainData['puts']['Volume'], errors = 'coerce')
    
    #get sum of volume
    totalVolume = chainData['calls']['Volume'].sum(
        ) + chainData['puts']['Volume'].sum()
    
    #save data to lists
    expirationDate.append(expDate.strftime('%m/%d/%Y'))
    daysToExpiration.append(DTE)
    totalVolumeByExpiration.append(totalVolume)
    
#data by expiration    
byExpirationData = pd.DataFrame(data = list(zip(
    expirationDate, daysToExpiration, totalVolumeByExpiration)),
    columns = ['Expiration Date', 'DTE', 'Total Volume'])
