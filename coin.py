import api
import requests
import db
import time
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

headers = {
    'X-CMC_PRO_API_KEY': api.api_key,
    'Accepts' : 'application/json', 
}

params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD',
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
json = requests.get(url, params=params, headers=headers).json()
coins = json['data']
symbol_select = input('>>>')
t = 5
def add_price(coin, price):
    c = db.Price(coin, price) 
    session.add(c)
    session.commit()

for info in coins:
    symbol = info['symbol']
    if symbol_select in symbol:
        while True:
            time.sleep(t)
            print(symbol_select, info['quote']['USD']['price'])
            add_price(symbol_select, info['quote']['USD']['price'])
    

session.close()