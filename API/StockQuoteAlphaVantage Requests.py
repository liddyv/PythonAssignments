# Getting a stock quote

import urllib.request
import json
import requests

API_KEY = 'Replace with your API key here'
#  Data provided for free by AlphaVantage.  Website:  alphavantage.co

def getStockData(symbol):

    #For hight usage function, go to https://www.alphavantage.co/documentation/
    #https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo
    response = requests.get(
        'https://www.alphavantage.co/query',
        params={'function':'BATCH_STOCK_QUOTES',
                      'symbols':symbol,
                      'apikey':API_KEY})

    # Convert from a json-style string to a Python dictionary
    quoteDict = json.loads(response.content)
    print(quoteDict)
    '''
    {'Meta Data': {'1. Information': 'Batch Stock Market Quotes', '2. Notes': 'IEX Real-Time', '3. Time Zone': 'US/Eastern'}, 
    'Stock Quotes': [{'1. symbol': 'OUT', '2. price': '26.6500', '3. volume': '752556', '4. timestamp': '2019-08-15 16:04:09'}]}
    '''
    stockDict = quoteDict['Stock Quotes'][0]
    
    # Get just the piece we want:
    return stockDict['1. symbol'], stockDict['2. price']

while True:
    print()
    userSymbol = input('Enter a stock symbol: ')
    if userSymbol == '':
        break
    theSymbol, price = getStockData(userSymbol)

    print()
    print('The current price of', theSymbol, 'is:', price)
    print()

print('OK bye')

    



