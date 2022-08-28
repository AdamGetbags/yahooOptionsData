# -*- coding: utf-8 -*-
"""
Get Options Data With yahoo_fin

@author: Adam Getbags
"""

#import modules
from yahoo_fin import options as op

#input ticker
ticker = 'PLTR'

#get expiration dates
expirationDates = op.get_expiration_dates(ticker)

#call and put option data
callData = op.get_calls(ticker, date = expirationDates[0])
putData = op.get_puts(ticker, date = expirationDates[0])

#chain data
chainData = op.get_options_chain(ticker, date = expirationDates[0])
