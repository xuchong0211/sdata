import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import numpy as np
import threading






today = date.today().strftime("%Y%m%d")
startDate = (date.today() + relativedelta(months=-8)).strftime("%Y%m%d")
# startDate = "20211201"

print( today)
print( startDate)

design_view = {
  "_id": "_design/months",
  "views": {
    "over": {
      "map": "function (doc) {\n  var data = doc.data;\n  if(data.length == 9) {\n    \n    var m1 = data[data.length-1];\n    var m2 = data[data.length-2];\n    // emit(doc._id, m2);\n    var shiti = m1.close - m1.open > 0 ? m1.close : m1.open;\n    if (m2.open > shiti) {\n      emit(doc._id, {ma1: m1, m2: m2});\n      \n      // for (var i =0 ; i < data.length; i++) {\n      //   var month = data[i]\n      // }\n      // emit(doc._id, 1);\n    }\n    \n  }\n}"
    },
    "jump": {
      "reduce": "_count",
      "map": "function (doc) {\n  var data = doc.data;\n  if(data.length == 9) {\n    \n    var m1 = data[data.length-1];\n    var m2 = data[data.length-2];\n    // emit(doc._id, m2);\n    // var shiti = m1.close - m1.open > 0 ? m1.close : m1.open;\n    if (m2.open > m1.high) {\n      emit(doc._id, m2);\n      \n      // for (var i =0 ; i < data.length; i++) {\n      //   var month = data[i]\n      // }\n      // emit(doc._id, 1);\n    }\n    \n  }\n}"
    }
  },
  "language": "javascript"
}

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
# db = couch.create('longterm_'+today)
db = couch['longterm_'+today]
stocks = ak.stock_zh_a_spot_em()


period="monthly"
# period="daily"
# period="weekly"



count=0

def saveStock(list):
    
    for stock in list:

        code=stock['code']
        name=stock['name']

        print("================================================" + code + name)
        print(stock)
        print("================================================")

        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period="monthly", start_date=startDate, end_date=today, adjust="qfq")
        # print(stock_zh_a_hist_df)

        print("start.........: " + name)
        # count = count + 1
        data=[]
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
            dateStart = ''.join(str.split(row[0], "-"))
            begin = dateStart[0:6]+'01'
            end = dateStart[0:6]+'07'
            dailyDataList = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=begin, end_date=end, adjust="qfq")
            #
            dailyData=[]
            #
            for index, row1 in dailyDataList.iterrows():
                dailyData.append({
                    'name': name,
                    'code': code,
                    'date': row1[0],
                    'open': row1[1],
                    'close': row1[2],
                    'high': row1[3],
                    'low': row1[4],
                    'volume': row1[5],
                    'turn': row1[6],
                    'zhenfu': row1[7],
                    'range': row1[8],
                    'amount': row1[9],
                    'turnover': row1[10],
                })

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
                'dailyData': dailyData
            })

        if len(data) > 0 :
            data.reverse()
            db.save({'_id':  data[0]["date"] + '_' + code,
                    'date': data[0]["date"],
                    'name': name,
                    'code': code,
                    'data': data,
                    })



stockList = []



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

    if len(stockList) > 50:
        t1 = threading.Thread(target=saveStock, args=(stockList,))
        t1.start()
        print("start thread........" + str(sindex))
        stockList=[]

if len(stockList) > 0:
    t1 = threading.Thread(target=saveStock, args=(stockList,))
    t1.start()
    print("start thread........" + str(sindex))
    stockList=[]

# 创建线程
# t1 = threading.Thread(target=saveStock, args=(1,))
# t2 = threading.Thread(target=saveStock, args=(2,))


print("............保存view.............")

db.save(design_view)

print("............完成.............")

