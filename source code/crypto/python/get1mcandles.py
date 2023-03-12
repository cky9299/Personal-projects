import requests
import datetime
import time

initOpen=0
initClose=0
initLow=0
initHigh=0

dataCurrencies=requests.get("https://api.huobi.pro/v1/common/currencys")
dataCurrenciesDict=dataCurrencies.json()['data']
for ticker in dataCurrenciesDict: #'data'=['usdt','btc',...]
    try:
        candleResponse=requests.get(
            "https://api.huobi.pro/market/history/kline?period=1min&size=1441&symbol="+ticker+"usdt")
        candleData=candleResponse.json()['data'] #check whether got 'data' key
        f=open('%s.txt'%ticker,'a')
        
        dataLen=len(candleData)
        for i in range(dataLen-1,0,-1): #ascending ts
            Open=candleData[i]['open']
            Close=candleData[i]['close']
            Low=candleData[i]['low']
            High=candleData[i]['high']
            if initOpen!=Open or initClose!=Close or initLow!=Low or initHigh!=High: #only log when price changes
                f.write(str(datetime.datetime.fromtimestamp(candleData[i]['id'])) + ', ' + str(candleData[i]['open']) + ', ' + str(candleData[i]['close']) + ', ' + str(candleData[i]['low']) + ', ' + str(candleData[i]['high']) + '\n')#id is unix timestamp in seconds
            initOpen=Open
            initClose=Close
            initLow=Low
            initHigh=High
        f.close()
    except KeyError:
        continue

