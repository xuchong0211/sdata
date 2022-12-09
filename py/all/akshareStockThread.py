import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta
import numpy as np

import threading

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# today = '20220901'
today = date.today().strftime("%Y%m%d")
startDate = (date.today() + timedelta(days=-180)).strftime("%Y%m%d")

# ipAddress = '192.168.23.30'
ipAddress = '127.0.0.1'
couch = couchdb.Server('http://admin:password@'+ipAddress+':5984/')
db = couch.create('daily_'+today + '_fast')



group = 200

period="daily"
# period="weekly"
# period="monthly"

count=0

def getZTList(list):

  a = np.array(list[0:len(list)-1])

  b = np.array(list[1:])

  ztlist = ""

  for i in range(len(a)) :
    zt = a[i]["close"] == round(b[i]["close"] * 1.1, 2)
    if zt :
      ztlist = ztlist + "1"
    else :
      ztlist = ztlist + "0"

  return ztlist

def calcMA(arr, window_size):
  # Program to calculate moving average

  i = 0
  # Initialize an empty list to store moving averages
  moving_averages = []

  # Loop through the array to consider
  # every window of size 3
  while i < len(arr) - window_size + 1:

      # Store elements from i to i+window_size
      # in list to get the current window
      window = arr[i : i + window_size]

      # Calculate the average of current window
      window_average = round(sum(window) / window_size, 2)

      # Store the average of current
      # window in moving average list
      moving_averages.append(window_average)

      # Shift window to right by one position
      i += 1

  print(moving_averages)
  return moving_averages


def calcMAEligible(arr, window_size):
  # Program to calculate moving average
  eligible = True
  value = 0

  i = 0
  # Initialize an empty list to store moving averages
  moving_averages = []

  # Loop through the array to consider
  # every window of size 3
  while i < len(arr) - window_size + 1:

      # Store elements from i to i+window_size
      # in list to get the current window
      window = arr[i : i + window_size]

      # Calculate the average of current window
      window_average = round(sum(window) / window_size, 2)

      if value==0 :
        value = window_average
      else :
        eligible = eligible and value >= window_average
      value = window_average

      # if eligible:
      #   eligible = arr[i] >= window_average

      # Store the average of current
      # window in moving average list
      moving_averages.append(window_average)

      # Shift window to right by one position
      i += 1

  print(moving_averages)

  return {"ma": moving_averages, "eligible":eligible}





def saveStock(list):

    for stock in list:

        code=stock['code']
        name=stock['name']

        print("start to save stock ================================================" , code , name, end='\n * ')

        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period=period, start_date=startDate, end_date=today, adjust="qfq")
        # print(stock_zh_a_hist_df)
        global count
        count = count + 1
        print("count:  " , count, end='\n')
        data=[]
        closeList=[]
        #
        for index, row in stock_zh_a_hist_df.iterrows():
            #     result = db.save(row)

            # 日期	object	交易日 0
            # 开盘	float64	开盘价 1
            # 收盘	float64	收盘价 2
            # 最高	float64	最高价 3
            # 最低	float64	最低价 4
            # 成交量	int32	注意单位: 手 5
            # 成交额	float64	注意单位: 元 6
            # 振幅	float64	注意单位: % 7
            # 涨跌幅	float64	注意单位: % 8
            # 涨跌额	float64	注意单位: 元 9
            # 换手率	float64	注意单位: % 10
            data.append({
                'name': name,
                'code': code,
                'date': row[0],
                'open': row[1],
                'close': row[2],
                'high': row[3],
                'low': row[4],
                'volume': row[5],
                'turn': row[6],
                'zhenfu': row[7],
                'range': row[8],
                'amount': row[9],
                'turnover': row[10],
            })
            closeList.append(row[2])

        if len(data) > 0 :
            data.reverse()
            closeList.reverse()

        ma5Data = calcMAEligible(closeList, 5)
        ma13Data = calcMAEligible(closeList, 13)
        ma34Data = calcMAEligible(closeList, 34)

        ma5 = ma5Data["ma"][0 : 20]
        ma13 = ma13Data["ma"][0 : 20]
        ma34 = ma34Data["ma"][0 : 20]

        ma5Up = ma5Data["eligible"]
        ma13Up = ma13Data["eligible"]
        ma34Up = ma34Data["eligible"]


        data = data[0 : 50]

        ztlist = getZTList(data)

        db.save({'_id':  data[0]["date"] + '_' + code,
                  'date': data[0]["date"],
                  'name': name,
                  'code': code,
                  'data': data,
                  'ma5': ma5,
                  'ma13': ma13,
                  'ma34': ma34,

                  'ma5Up': ma5Up,
                  'ma13Up': ma13Up,
                  'ma34Up': ma34Up,
                  'ztlist': ztlist
                  })

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


      stockList.append({
          'name': name,
          'code': code
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

design_view = {
  "_id": "_design/list",
  "views": {
    "diao": {
      "map": "function (doc) {\n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var small1 = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var small2 = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var small3 = day3.open > day3.close && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n      \n      var small4 = day4.open < day4.close && Math.abs(day4.open - day4.close)/day4.open > 0.04;\n      \n      var gaokai = day3.open > day4.close || day2.open > day3.close;\n      //emit([doc.date, doc.code], {name: doc.name});\n      if (small1 && small2 && small3 && small4) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    },
    "feilong": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var overall =  day1.close > day1.open && day1.close > day2.close && day1.close > day3.close && day1.close > day4.close;\n      \n      //var small2 = day2.open < day2.close;// && Math.abs(day2.open - day2.close)/day2.open > 0.005;\n      var smallSolid =  Math.abs(day2.open - day2.close)/day2.open < 0.05;\n      \n      var gaokai = day2.open > day3.close;\n      \n      var tiaokong = day2.low > day3.high;\n      \n      var zhangting = day3.range > 9.9299;\n     \n      if (overall && smallSolid && zhangting && gaokai && tiaokong) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "flower": {
      "map": "function (doc) {\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      //emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var solid = Math.abs(day1.open - day1.close)/day1.open > 0.01;\n      \n      var smallSolid = Math.abs(day2.open - day2.close)/day2.open <= 0.005;\n      \n      var threeGao = day1.close > day2.close && day1.high > day2.high && day1.low > day2.low;\n      \n      var stand = day3.low < day2.low;\n      \n      if (solid && smallSolid && threeGao && stand) {\n        emit([doc.date, doc.code], {code: doc.code, name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    },
    "doublelong": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var volume = day2.volume > day3.volume && day2.volume > day1.volume;\n      \n      var zhangting = day1.range > 9.9299 && day2.range > 9.9299;\n     \n      if (zhangting && volume) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "falmerjianlong": {
      "map": "function (doc) {\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var overall = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n      \n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var smallSolid = day2.open > day2.close //&& Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var gaokai = day2.open > day3.close && day2.close < day3.close;\n      \n      //var stand = day4.open < day1.low && day4.open < day2.low && day4.open < day3.low;\n      \n      //A\n      var day3Red = day3.open < day3.close;// && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n      \n      //B\n      //var day3Green = day3.open > day3.close && Math.abs(day3.open - day3.close)/day2.open < 0.03;\n      \n      \n      if (overall && smallSolid && gaokai && day3Red) {\n        emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: day1.open, close: day1.close });\n      }\n    }\n  }\n}"
    },
    "dayou": {
      "map": "function (doc) {\n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      var day5 = data[4];\n      var day6 = data[5];\n      var day7 = data[6];\n      \n      var overall = day1.open < day1.close && day1.close > day2.open && day1.close > day3.close && day1.close > day4.close && day1.close > day5.close && day1.close > day6.close;\n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var small2 = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var red = day3.open < day3.close && day4.open < day4.close && day5.open < day5.close  && day6.open < day6.close && day7.open > day7.close;\n      \n      // var gaokai = day3.open > day4.close || day2.open > day3.close;\n      //emit([doc.date, doc.code], {name: doc.name});\n      if (overall && small2 && red) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    },
    "jianlongplus": {
      "map": "function (doc) {\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var overall = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n      \n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var smallSolid = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var gaokai = day2.open > day3.close;\n      \n      var stand = day4.open < day1.low && day4.open < day2.low && day4.open < day3.low;\n      \n      //A\n      var day3Red = day3.open < day3.close;// && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n      \n      //B\n      var day3Green = day3.open > day3.close && Math.abs(day3.open - day3.close)/day2.open < 0.03;\n      \n      \n      if (overall && smallSolid && gaokai && stand && (day3Red || day3Green)) {\n        emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: day1.open, close: day1.close });\n      }\n    }\n  }\n}"
    },
    "jianlong": {
      "map": "function (doc) {\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var overall = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n      \n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var smallSolid = day2.open > day2.close //&& Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var gaokai = day2.open > day3.close;\n      \n      //var stand = day4.open < day1.low && day4.open < day2.low && day4.open < day3.low;\n      \n      //A\n      var day3Red = day3.open < day3.close;// && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n      \n      //B\n      //var day3Green = day3.open > day3.close && Math.abs(day3.open - day3.close)/day2.open < 0.03;\n      \n      \n      if (overall && smallSolid && gaokai && day3Red) {\n        emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: day1.open, close: day1.close });\n      }\n    }\n  }\n}"
    },
    "feihuiluzhuan": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"30\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var volume = day2.volume > day3.volume && day2.volume > day1.volume;\n      \n      var zhangting = day2.range > 9.9299;\n      \n      var small2 = day2.close > day1.close;\n     \n      if (zhangting && small2 && volume) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "gesandaniu": {
      "map": "function (doc) {\n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      var day5 = data[4];\n      \n      \n      var bigred = day4.open < day4.close && Math.abs(day4.open - day4.close)/day4.open > 0.03;\n      \n      var bigVolume = day4.volume / day5.volume >1.1;\n      \n      \n      var volume1 = day1.volume < day4.volume;\n      var volume2 = day2.volume < day4.volume;\n      var volume3 = day3.volume < day4.volume;\n      \n      var volumeDown = volume1 && volume2 && volume3;\n      \n      var over1 = day4.open < day1.close;\n      var over2 = day4.open < day2.close;\n      var over3 = day4.open < day3.close;\n      \n      //emit([doc.date, doc.code], {name: doc.name});\n      if (bigred && bigVolume && over1 && over2 && over3 && volumeDown) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    },
    "gesandaniuplus": {
      "map": "function (doc) {\n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      var day5 = data[4];\n      \n      \n      var bigred = day4.open < day4.close && Math.abs(day4.open - day4.close)/day4.open > 0.03;\n      \n      var bigVolume = day4.volume / day5.volume >2;\n      \n      var over1 = day4.open < day1.close;\n      var over2 = day4.open < day2.close;\n      var over3 = day4.open < day3.close;\n      \n      var count = 0;\n      \n      if (day4.close < day1.close) {\n        count = count + 1\n      }\n      \n      if (day4.close < day2.close) {\n        count = count + 1\n      }\n      \n      if (day4.close < day3.close) {\n        count = count + 1\n      }\n      \n      \n      \n      var volume1 = day1.volume < day4.volume;\n      var volume2 = day2.volume < day4.volume;\n      var volume3 = day3.volume < day4.volume;\n      \n      var volumeDown = volume1 && volume2 && volume3;\n      \n      //emit([doc.date, doc.code], {name: doc.name});\n      if (bigred && bigVolume && over1 && over2 && over3 && count > 2 && volumeDown) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    },
    "shenlong3": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      //var day4 = data[3];\n      \n      var volume = day2.volume > day3.volume && day2.volume > day1.volume;\n      \n      var zhangting = day3.range > 9.9299;\n      \n      var virant = day2.zhenfu > 5 && day2.open < day2.close;\n      \n      var small1 = day1.open < day1.close && Math.abs(day1.open - day1.close)/day1.open < 0.03;\n     \n      if (zhangting && volume && virant && small1) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "fankeweizhuplus": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"30\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var big2 = day2.zhenfu >= 5 || day2.range <= -4;\n      \n      var green = day2.open > day2.close && day3.open < day3.close;\n      \n      var red1 = day1.open > day2.close && day1.range >= 5;\n      \n     \n      if (big2 && green && red1) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "shenqijunxian": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var ma5 = doc.ma5;\n    \n    var ma13 = doc.ma13;\n    \n    var ma34 = doc.ma34;\n    \n    var data = doc.data;\n    \n    \n    var m513 = ma5[0] > ma13[0] && ma5[1] < ma13[1];\n    \n    var crossIndex = 0;\n    var over34 = ma34[0] < ma13[0] && ma34[0] < ma5[0] && ma34[0] < data[0].close && ma34[1] < ma13[1] && ma34[1] < ma5[1] && ma34[1] < data[1].close;\n    \n    var ma34rate = 1;\n    \n    // emit([doc.code], {m513: m513, over34: over34 });\n    \n    // emit([doc.code], {name: doc.name, code: doc.code, open: data[0].open, close: data[0].close });\n    if (m513 && over34) {\n      // emit([doc.code], {name: doc.name, code: doc.code, open: data[0].open, close: data[0].close });\n      \n      for(var i=2;i<ma34.length-1;i++) {\n        \n        ma34rate = Math.min(ma34rate, (ma5[i]-ma34[i])/ma34[i])\n        \n        if(crossIndex == 0 && ma5[i] < ma13[i] && ma5[i+1] > ma13[i+1]) {\n          crossIndex = i;\n        }\n        over34 = over34 && ma34[i] < ma13[i] && ma34[i] < ma5[i] && ma34[i] < data[i].close;\n      }\n      // emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: data[0].open, close: data[0].close, m513: m513, over34: over34, crossIndex: crossIndex });\n      if (crossIndex <= 20 && over34 && ma34rate < 0.05) {\n          emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: data[0].open, close: data[0].close, m513: m513, over34: over34, crossIndex: crossIndex,ma34rate:ma34rate });\n      }\n    }\n  }\n  \n}"
    },
    "shenlong1": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var ztlist = doc.ztlist;\n    \n    \n    var klist = \"0\" + doc.ztlist.substr(1);\n    \n    \n    var hengpanList = klist.split(\"1\");\n    \n    \n    if (hengpanList.length == 2) {\n      \n      \n      var data = doc.data;\n      var ztIndex = klist.indexOf(\"1\");\n      // emit([doc.date, doc.code], {hengpanList: hengpanList, ztIndex: ztIndex});\n      \n      \n      if (hengpanList[0].length >= 5) {\n        \n        \n        \n        \n        var ztClose = data[ztIndex].close;\n        var ztOpen = data[ztIndex].open;\n        var xipan = hengpanList[0].split(\"\").reverse();\n        var overClose = data[ztIndex-1].close > ztClose;\n        var count = overClose ? 1 : 0;\n        \n        \n        var shiti =  (ztClose - ztOpen)/ztOpen > 0.05;\n        \n        var eligible = data[0].close >= ztClose && data[0].close > data[0].open;\n        \n        \n        // if (false) {\n        //   emit([doc.date, doc.code, doc.name], {name: doc.name, code: doc.code, close: data[0].close, ztIndex: ztIndex, ztCLose: ztClose, overClose: overClose });\n        \n        // }\n        \n        \n        for(var i=1;i<xipan.length-1;i++) {\n          var dayData = data[ztIndex - 1 - i];\n          if (overClose) {\n            if (dayData.close > ztClose) {\n              count = count + 1;\n              if (count > 5) {\n                eligible = false;\n                break;\n              }\n            } else {\n              overClose = false;\n            }\n          } else {\n            if (dayData.close > ztClose || dayData.close < ztOpen) {\n              eligible=false;\n              break;\n            }\n          }\n          \n          \n          \n          // if (!downClose && xipan[0].close > ztClose) {\n          //   count = count + 1;\n          //   if (count > 5) {\n          //     eligible = false;\n          //     break;\n          //   }\n          // } else {\n          //   downClose = true;\n          // }\n        }\n        \n        \n        \n        if (eligible) {\n          emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: data[0].open, close: data[0].close, ztIndex: ztIndex, ztCLose: ztClose });\n        \n        }\n      }\n      \n    }\n  }\n  \n}"
    },
    "yiyidailao": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      \n      var day2 = data[1];\n      \n      var day3 = data[2];\n      var day4 = data[3];\n      var day5 = data[4];\n      \n      var day6 = data[5];\n      \n      var volume = day6.volume > day5.volume && day5.volume > day4.volume  && day4.volume > day3.volume;\n      \n      var red = day6.open < day6.close && day2.open < day2.close && day1.close > day1.open;\n      \n      var green = day3.open > day3.close && day4.open > day4.close && day5.open > day5.close;\n      \n      var high =  day5.high > day4.high  && day4.high > day3.high;\n      \n      var low =  day5.low > day4.low  && day4.low > day3.low;\n      \n      var over = day1.close > day2.close ;\n     \n      if (red && green && high && low && over && volume) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "vmodel": {
      "map": "function (doc) {\n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 14) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      // var day2 = data[1];\n      // var day3 = data[2];\n      // var day4 = data[3];\n      // var day5 = data[4];\n      // var day6 = data[5];\n      // var day7 = data[6];\n      // var day8 = data[7];\n      // var day9 = data[8];\n      // var day10 = data[9];\n      // var day11 = data[10];\n      // var day12 = data[11];\n      // var day13 = data[12];\n      // var day14 = data[13];\n      \n      // var list = [day14, day13, day12, day11, day10, day9, day8, day7, day6, day5, day4, day3, day2, day1];\n      \n      var list = [];\n      \n      for(var i=13; i >= 0 ;i--) {\n        list.push(data[i].close >= data[i].open);\n      }\n      \n      var continueGreenCount = 0;\n      \n      var continueRedCount = 0;\n      \n      var red = false;\n      \n      var green = false;\n      \n      for(var j=0; j < list.length ;j++) {\n        \n        if (continueRedCount > 3) {\n          red = true;\n        }\n        \n        if (continueGreenCount > 3) {\n          green = true;\n        }\n        \n        var amount = list[j];\n        if (amount) {\n          continueRedCount = continueRedCount + 1;\n          continueGreenCount = 0;\n        } else {\n          continueGreenCount = continueGreenCount + 1;\n          continueRedCount = 0;\n        }\n        \n      }\n      \n      \n      // for(var k=0; k < list.length ;k++) {\n      //   var amount1 = list[k];\n      //   if (amount1 >= 0) {\n      //     continueGreenCount = 0;\n      //   } else {\n      //     continueGreenCount = continueGreenCount + 1;\n      //   }\n        \n      //   if (continueGreenCount > 2) {\n      //     green = true;\n      //   }\n      // }\n      \n      \n      \n      // emit([doc.date, doc.code], {red: red, green: green, list:list});\n      \n      if (red && green) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close, list:list});\n      }\n    }\n  }\n  \n  \n}"
    }
  },
  "language": "javascript"
}

db.save(design_view)

print("............模型导入完成...........")


print("............结束...........")
