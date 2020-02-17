import requests 
import json
import talib
import numpy 
import pandas
import datetime
import time


def callWxInfo(topic,price):
    info = topic+ '\r\n'+price
    pusher = 'http://wxpusher.zjiecode.com/api/send/message/?appToken=AT_uWm4moKaCgKCGNrOUsCEbBI1A5IrElpx&uid=UID_KUJzRO0bmJxZCWXsIRmUsRX2Zsv3&content=' + info
    requests.get(pusher)


def callLastTimtInfo(endTime):
    baseHost = 'https://www.okex.me'
    queryCandlesURI = '/api/spot/v3/instruments/BTC-USDT/candles?granularity=86400&end=%sT16:30:01.000Z' % (endTime)
    responseData = requests.get(baseHost+queryCandlesURI).json()
    print(responseData[0][0])

def caculateOperation(endTime):
    # step0:采集原始数据
    # 数据格式:time/open/high/low/close/volume
    baseHost = 'https://www.okex.me'
    queryCandlesURI = '/api/spot/v3/instruments/BTC-USDT/candles?granularity=86400&end=%sT16:30:01.000Z' % (endTime)
    responseData = requests.get(baseHost+queryCandlesURI).json()
    df = pandas.DataFrame(responseData,columns=['time','open','high','low','close','volume'])
    df = df.sort_index(ascending=False)


    # step1:计算EMA和MACD指标
    closeArray = [float(x) for x in df['close']]
    df['EMA12'] = talib.EMA(numpy.array(closeArray),timeperiod=12)
    df['EMA26'] = talib.EMA(numpy.array(closeArray),timeperiod=26)
    df['dif'],df['dem'],df['histogram'] = talib.MACD(numpy.array(closeArray),fastperiod=12, slowperiod=26, signalperiod=9)
    df = df.sort_index()

    # step2:执行对应的策略
    # 指标MACD策略
    #策略1:histogram跨越0轴，提示买入卖出
    if df['histogram'][0] * df['histogram'][1] < 0:
        if df['histogram'][0] >= 0:
            print('1- buy now ' + df['time'][0]+' '+df['close'][0])
            callWxInfo('买信号 跨越0轴',str('时间：'+df['time'][0] +'收盘价：'+ df['close'][0] +'最高价：'+ df['high'][0] +'最低价：'+ df['low'][0]))
        else:
            print('1- sale now ' + df['time'][0]+' '+df['close'][0])
            callWxInfo('卖信号 跨越0轴',str('时间：'+df['time'][0] +'收盘价：'+ df['close'][0] +'最高价：'+ df['high'][0] +'最低价：'+ df['low'][0]))
    #策略2:histogram趋势被打破，提示买入卖出
    if df['histogram'][0] < 0:
        if ((df['histogram'][1] < df['histogram'][0]) & (df['histogram'][2] > df['histogram'][1])):
            print('2- buy now ' + df['time'][0]+' '+df['close'][0])
            callWxInfo('买信号 趋势打破',str('时间：'+df['time'][0] +'收盘价：'+ df['close'][0] +'最高价：'+ df['high'][0] +'最低价：'+ df['low'][0]))
    elif df['histogram'][0] > 0:
        if ((df['histogram'][1] > df['histogram'][0]) & (df['histogram'][2] < df['histogram'][1])):
            print('2- sale now '  + df['time'][0]+' '+df['close'][0])
            callWxInfo('卖信号 趋势打破',str('时间：'+df['time'][0] +'收盘价：'+ df['close'][0] +'最高价：'+ df['high'][0] +'最低价：'+ df['low'][0]))
    return 'success'

# step3:对当前数据进行回测
# start = datetime.datetime(2019,1, 1, 12, 0, 0)
# for i in range(365):
#     caculateOperation(str(start)[0:10])
#     start = start + datetime.timedelta(days=1)

# step4:启动程序开始执行
while(1):
    # 8点和20点执行一次
    nowHour = str(datetime.datetime.now())[11:13]
    callLastTimtInfo(str(datetime.datetime.now())[0:10])
    print('job执行当前时间'+str(datetime.datetime.now()))
    if ( nowHour == '01'):
        caculateOperation(str(datetime.datetime.now())[0:10])
    if (nowHour == '08'):
        caculateOperation(str(datetime.datetime.now())[0:10])
    if ( nowHour == '20'):
        caculateOperation(str(datetime.datetime.now())[0:10])
    time.sleep(3600)










