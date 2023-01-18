import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta
import numpy as np
import requests

import threading

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# today = '20220901'
today = date.today().strftime("%Y%m%d")
# startDate = (date.today() + timedelta(days=-180)).strftime("%Y%m%d")

# ipAddress = '192.168.23.30'
ipAddress = '127.0.0.1'
couch = couchdb.Server('http://admin:password@'+ipAddress+':5984/')
# db = couch.create('daily_'+today + '_fast')
observeDB = couch.create('daily_'+today + '_observe')



group = 200

period="daily"
# period="weekly"
# period="monthly"

count=0


def saveStock(list):

    for stock in list:

        code=stock['code']
        name=stock['name']
        price=stock['price']
        high=stock['high']
        low=stock['low']

        print("start to save observe stock ================================================" , code , name, price, end='\n * ')


        url = 'http://'+ipAddress+':5984/observe/_design/stock/_view/list?key=\"'+code+'\"'
        # print("url 111111111111111111111", url)
        res = requests.get(url)
        # print("res 22222222222222222", res)

        data = res.json()
        # print("data 333333333333333333333", data)
        data = data["rows"]


        for item in data:
            targetPrice = item['value']['price']
            targetDate = item['value']['date']
            fromDate = item['value']['fromDate']
            action = item['value']['action']
            print("data 44444444444444444444444", data)
            print("data 5555555555555555555", targetPrice, low, high)
            # print("data 5555555555555555555", item)


            if targetPrice >= low and targetPrice <= high :
                print("66666666666666666666666")
                saveData = {'_id':  today + '_' + code,
                            'date': today,
                            'name': name,
                            'code': code,
                            'price': price,
                            'high': high,
                            'low': low,
                            'target': targetPrice,
                            'targetDate': targetDate,
                            'fromDate': fromDate,
                            'action': action,
                            }
                print("777777777777777777777", saveData)

                observeDB.save({
                    # '_id':  today + '_' + code,
                          'date': today,
                          'name': name,
                          'code': code,
                          'price': price,
                          'high': high,
                          'low': low,
                          'target': targetPrice,
                          'targetDate': targetDate,
                          'fromDate': fromDate,
                          'action': action,
                          })
            print("88888888888888888888888888")

#get today stocks
if True :
  stockList = []

  stocks = ak.stock_zh_a_spot_em()

  for sindex, srow in stocks.iterrows():

  # 名称	类型	描述
  # 序号	int64	-
  # 代码	object	-
  # 名称	object	-
  # 最新价	float64	-
  # 涨跌幅	float64	注意单位: %
  # 涨跌额	float64	-
  # 成交量	float64	注意单位: 手
  # 成交额	float64	注意单位: 元
  # 振幅	float64	注意单位: %
  # 最高	float64	-
  # 最低	float64	-
  # 今开	float64	-
  # 昨收	float64	-
  # 量比	float64	-
  # 换手率	float64	注意单位: %
  # 市盈率-动态	float64	-
  # 市净率	float64	-
  # 总市值	float64	注意单位: 元
  # 流通市值	float64	注意单位: 元
  # 涨速	float64	-
  # 5分钟涨跌	float64	注意单位: %
  # 60日涨跌幅	float64	注意单位: %
  # 年初至今涨跌幅	float64	注意单位: %
      code = srow[1]
      name = srow[2]
      price = srow[3]
      high = srow[9]
      low = srow[10]


      stockList.append({
          'name': name,
          'code': code,
          'price': price,
          'high': high,
          'low': low
      })


      if len(stockList) >= group:
          t1 = threading.Thread(target=saveStock, args=(stockList,))
          t1.start()
          print("start thread =====================> " , sindex, end='\n')
          stockList=[]

  if len(stockList) > 0:
      t1 = threading.Thread(target=saveStock, args=(stockList,))
      t1.start()
      print("start thread =====================> last", end='\n')
      stockList=[]
else :
  print("222222222222222222222222222222222", end='\n')
  saveStock([{
          'name': "中路股份",
          'code': "600818"
      }])




print("............下载完成 : ", count , "...........", end="\n")

observe_design_view = {
    "_id": "_design/stock",
    "_rev": "3-3ea56223304702a5f949c26ccb07574f",
    "views": {
        "list": {
            "map": "function (doc) {\n  var code = doc._id;\n  var observe = doc.observe;\n  for(var i=0; i< observe.length;i++) {\n    var data = observe[i];\n    \n      // \"fromDate\": 20190228,\n      // \"date\": 20230118,\n      // \"price\": 5.17,\n      // \"action\": \"buy\"\n    emit(doc._id, {code: code, fromDate:data.fromDate, date: data.date, price: data.price, action: data.action});\n  }\n}"
        }
    },
    "language": "javascript"
}

observe_sample_data = {
    "_id": "600892",
    "_rev": "3-507f959d8d0029bfe3605275c4d4fa3e",
    "name": "大晟文化",
    "observe": [
        {
            "fromDate": 20190228,
            "date": 20230118,
            "price": 5.17,
            "action": "buy"
        }
    ]
}

# db.save(design_view)


print("............结束...........")
