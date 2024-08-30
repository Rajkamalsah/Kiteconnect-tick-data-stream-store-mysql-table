
"""
Created on Tue Feb  7 17:16:44 2023

@author: Raj
"""
#access the generated access token
import pymysql
from kiteconnect import KiteTicker
import os 
from kiteconnect import KiteConnect

cwd = os.chdir("E:\\a\\b\\c")
access_token=open("access_token.txt",'r').read()
key_secret=open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key = key_secret[0])
kite.set_access_token(access_token)

kws = KiteTicker(key_secret[0],kite.access_token) #this object will stream data for us




#%%
#access the created table
db=pymysql.connect(host='a',user='b',password='',database='c')
#dict={341249:'HDFCBANK',738561:'RELIANCE',408065:'INFY',340481:'HDFC',1270529:'ICICIBANK'}
insert_into_table='insert into banknifty(tradingsymbol,LTP,date) values(%(tradingsymbol)s,%(LTP)s,%(date)s)'

def insert_ticks3(ticks):
    for tick in ticks:
        try:
            a = tick['instrument_token']
        except:
            a = 0
        try:
            b = tick['last_price']
        except:
            b = 0
        
        try:
            e = tick['exchange_timestamp']
        except:
            e = 0
            
    c=db.cursor()
    c.execute(insert_into_table,{'tradingsymbol':a,'LTP':b,'date':e})
    try:
        db.commit()
    except Exception:
        db.rollback()
   
#%%




#access the banknifty and nifty values and store those in previous table
tokens=[260105]





def on_ticks(ws,ticks):
    
    # Callback to receive ticks.
    #logging.debug("Ticks: {}".format(ticks))
     
     insert_tick3=insert_ticks3(ticks)
     print(ticks)
    
def on_connect(ws,response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    #logging.debug("on connect: {}".format(response))
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL,tokens) # Set all token tick in `full` mode.
    #ws.set_mode(ws.MODE_FULL,[tokens[0]])  # Set one token tick in `full` mode.
 

kws.on_ticks=on_ticks
kws.on_connect=on_connect
kws.connect(threaded=True) #if you want to run this program in background in console the put kws.connect(threaded=True) in stead kws.connect()


