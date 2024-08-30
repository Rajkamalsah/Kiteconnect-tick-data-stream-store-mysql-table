# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:35:00 2023

@author: Raj
"""

import mysql.connector as sql
import pandas as pd
import numpy as np
db=sql.connect(host='a',user='b',password='c',database='d')
data=pd.read_sql('select *from ticks',con=db,parse_dates=True)
data=pd.DataFrame(data)
data=data.set_index(['date'])
ticks=data.ix[:,['last_price']]
#data=ticks['last_price'].resample('1min').ohlc().dropna()
print(data['close'])