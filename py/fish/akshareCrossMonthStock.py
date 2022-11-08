import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta
import numpy as np
from statistics import mean
import threading

today = date.today().strftime("%Y%m%d")
# today = '20220831'
# startDate = (date.today() + timedelta(weeks=-90)).strftime("%Y%m%d")
startDate = '19900101'

# design_view = {
#   "_id": "_design/g8",
#   "views": {
#     "mai1_3": {
#       "reduce": "_count",
#       "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var week0 = doc.weeks[0];\n    \n    var week1 = doc.weeks[1];\n    \n    var week2 = doc.weeks[2];\n    \n    var week3 = doc.weeks[3];\n    \n    var ma10 = doc.m10;\n    var ma60 = doc.m60;\n    \n    var goldCross = false;\n    \n    var over = week0.close > ma60[0];\n    \n    var up = ma60[0] > ma60[1];\n    \n    var bigRed = false;\n    \n    for(var i=0; i < 3; i++) {\n      if(ma10[i] >= ma60[i] && ma10[i+1] < ma60[i+1]) {\n      // if(ma10[i] >= ma60[i]) {\n        goldCross = true;\n      }\n      \n      \n      if(doc.weeks[i].range >= 5 && doc.weeks[i].close > doc.weeks[i].open) {\n        bigRed = true;\n      }\n    }\n    \n    \n      // emit([doc.date,doc.code,doc.name], {a: goldCross, b:bigRed, c:over});\n    \n    if (goldCross && bigRed && over && up) {\n      emit([doc.date,doc.code,doc.name],  {code: doc.code,name: doc.name, open: week0.open, close: week0.close});\n    }\n  }\n  \n  \n  \n}"
#     },
#     "mai2_3": {
#       "map": "function (doc) {\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n      var weeks = doc.weeks;\n  \n    var week0 = weeks[0];\n    \n    var week1 = weeks[1];\n    \n    var week2 = weeks[2];\n    \n    var week3 = weeks[3];\n    \n    var ma10 = doc.m10;\n    var ma60 = doc.m60;\n    \n    var stand = ma10[3] > ma60[3];\n    \n    var closeNear = Math.abs((weeks[3].close - ma60[3])) / ma60[3];\n    \n    var openNear = Math.abs((weeks[3].open - ma60[3])) / ma60[3];\n    \n    var lowNear = Math.abs((weeks[3].low - ma60[3])) / ma60[3];\n    \n    var over = week0.close > ma60[0];\n    \n    var up = true;\n    \n    var bigRed = false;\n    \n    for(var i=0; i < 3; i++) {\n      \n      var nearClosei = Math.abs((weeks[i].close - ma60[i])) / ma60[i];\n      \n      if (nearClosei < closeNear) {\n        closeNear = nearClosei;\n      }\n      \n      var nearOpeni = Math.abs((weeks[i].open - ma60[i])) / ma60[i];\n      \n      if (nearOpeni < openNear) {\n        openNear = nearOpeni;\n      }\n      \n      var nearLowi = Math.abs((weeks[i].low - ma60[i])) / ma60[i];\n      \n      if (nearLowi < lowNear) {\n        lowNear = nearLowi;\n      }\n      \n      if(ma60[i] < ma60[i+1]) {\n        up = false;\n      }\n      \n      \n      // if(weeks[i].close < ma60[i]) {\n      //   over = false;\n      // }\n      \n      \n      \n      if(ma10[i] < ma60[i]) {\n        stand = false;\n      }\n      \n      if(weeks[i].close < ma60[i]) {\n        stand = false;\n      }\n      \n      \n      if(weeks[i].range >= 5 && weeks[i].close > weeks[i].open) {\n        bigRed = true;\n      }\n    }\n    \n    \n      // emit([doc.date,doc.code,doc.name], {stand: stand, bigRed:bigRed, over:over, up:up});\n    var near = closeNear < 0.03 || openNear < 0.03  || lowNear < 0.03;\n    if (near && stand && bigRed && over && up) {\n      emit([doc.date,doc.code,doc.name],  {code: doc.code,name: doc.name, open: week0.open, close: week0.close, near: near});\n    }\n  \n  }\n\n  \n  \n}"
#     }
#   },
#   "language": "javascript"
# }




couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
db = couch.create('crossmonth_'+today)
# db = couch['crossmonth']

group = 200

period="monthly"
# period="daily"
# period="weekly"


count=0

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
        #
        if len(stock_zh_a_hist_df) > 30 :
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


            # if len(data) > 0 :
            #     data.reverse()

            # data = data[0 : 50]


            db.save({'_id':  data[len(data)-1]["date"] + '_' + code,
                    'date': data[len(data)-1]["date"],
                    'name': name,
                    'code': code,
                    'data': data,
                    })



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


# saveStock([{
#         'name': "平安银行",
#         'code': "000001"}])


print("............start analysis.............", len(stockList))

# db.save(design_view)

print("............end.............")

