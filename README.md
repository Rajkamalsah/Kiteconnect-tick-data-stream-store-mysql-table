# Real-Time Data Fetching, Storing, and Processing with Kite Connect and MySQL

This project demonstrates how to fetch real-time market data using Kite Connect, store it in a MySQL database, and perform real-time processing. The project is divided into two main scripts: `kiteconnector-banknifty` for fetching and storing data, and `mysql_connector` for processing and analyzing the stored data.

## Features

- **Real-Time Data Fetching**: Fetch real-time market data using Kite Connect.
- **Data Storage**: Store the fetched data in a MySQL database.
- **Real-Time Processing**: Process the data in real-time and perform analysis.

## Tools and Technologies

- **Python**
- **Kite Connect**
- **MySQL**
- **Pandas**
- **NumPy**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/realtime-data-processing.git
    cd realtime-data-processing
    ```

2. Install the required libraries:
    ```bash
    pip install pymysql kiteconnect pandas numpy
    ```

3. Set up your MySQL database and update the connection details in the code.

## Usage

### Script `kiteconnector-banknifty`

This script fetches real-time market data using Kite Connect and stores it in a MySQL database.

```python
import pymysql
from kiteconnect import KiteTicker
import os 
from kiteconnect import KiteConnect

cwd = os.chdir("E:\\a\\b\\c")
access_token = open("access_token.txt", 'r').read()
key_secret = open("api_key.txt", 'r').read().split()
kite = KiteConnect(api_key=key_secret)
kite.set_access_token(access_token)

kws = KiteTicker(key_secret, kite.access_token)  # this object will stream data for us

# Access the created table
db = pymysql.connect(host='a', user='b', password='', database='c')
insert_into_table = 'insert into banknifty(tradingsymbol,LTP,date) values(%(tradingsymbol)s,%(LTP)s,%(date)s)'

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
            
        c = db.cursor()
        c.execute(insert_into_table, {'tradingsymbol': a, 'LTP': b, 'date': e})
        try:
            db.commit()
        except Exception:
            db.rollback()

# Access the banknifty and nifty values and store those in previous table
tokens = 

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    insert_ticks3(ticks)
    print(ticks)
    
def on_connect(ws, response):
    # Callback on successful connect.
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL, tokens)  # Set all token tick in `full` mode.

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect(threaded=True)  # if you want to run this program in background in console, use kws.connect(threaded=True)
