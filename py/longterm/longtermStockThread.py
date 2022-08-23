import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
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


today = date.today().strftime("%Y%m%d")
startDate = (date.today() + relativedelta(months=-8)).strftime("%Y%m%d")
# startDate = "20211201"

print( today)
print( startDate)

design_view = {
    "_id": "_design/months",
    "views": {
        "over": {
            "map": "function (doc) {\n  var data = doc.data;\n  if(data.length == 9) {\n    \n    var m0 = data[data.length-1];\n    var m1 = data[data.length-2];\n    \n    var m2 = data[data.length-3];\n    var m3 = data[data.length-4];\n    \n    var m4 = data[data.length-5];\n    var m5 = data[data.length-6];\n    \n    var m6 = data[data.length-7];\n    var m7 = data[data.length-8];\n    \n    // emit(doc._id, m2);\n    var shiti = m0.close - m0.open > 0 ? m0.close : m0.open;\n    if (m1.open > shiti) {\n      var buy = m1.dailyData[1].open;\n      \n      var diff1 = parseFloat(m1.close - buy).toFixed(2);\n      var diff1Ratio = parseFloat(diff1 / buy).toFixed(2);\n      \n      \n      var diff2 = parseFloat(m2.close - buy).toFixed(2);\n      var diff2Ratio = parseFloat(diff2 / buy).toFixed(2);\n      \n      \n      \n      var diff3 = parseFloat(m3.close - buy).toFixed(2);\n      var diff3Ratio = parseFloat(diff3 / buy).toFixed(2);\n      \n      \n      \n      var diff4 = parseFloat(m4.close - buy).toFixed(2);\n      var diff4Ratio = parseFloat(diff4 / buy).toFixed(2);\n      \n      \n      \n      var diff5 = parseFloat(m5.close - buy).toFixed(2);\n      var diff5Ratio = parseFloat(diff5 / buy).toFixed(2);\n      \n      \n      \n      var diff6 = parseFloat(m6.close - buy).toFixed(2);\n      var diff6Ratio = parseFloat(diff6 / buy).toFixed(2);\n      \n      \n      \n      var diff7 = parseFloat(m7.close - buy).toFixed(2);\n      var diff7Ratio = parseFloat(diff7 / buy).toFixed(2);\n      \n      \n      \n      \n      emit(doc._id, {name: doc.name,\n      code: doc.code,\n      m1open: m1.open,\n      m12open: m0.open,\n      m12high: m0.high,\n      openDiff: parseFloat(m0.open - m1.open).toFixed(2),\n      m12close: m0.close,\n      closeDiff: parseFloat(m0.close - m1.open).toFixed(2),\n      \n      buy: buy,\n      \n      close1: m1.close,\n      diff1: diff1,\n      diff1Ratio: diff1Ratio,\n      \n      \n      close2: m2.close,\n      diff2: diff2,\n      diff2Ratio: diff2Ratio,\n      \n      \n      close3: m3.close,\n      diff3: diff3,\n      diff3Ratio: diff3Ratio,\n      \n      \n      close4: m4.close,\n      diff4: diff4,\n      diff4Ratio: diff4Ratio,\n      \n      \n      close5: m5.close,\n      diff5: diff5,\n      diff5Ratio: diff5Ratio,\n      \n      \n      close6: m6.close,\n      diff6: diff6,\n      diff6Ratio: diff6Ratio,\n      \n      \n      close7: m7.close,\n      diff7: diff7,\n      diff7Ratio: diff7Ratio,\n      \n      \n        \n        \n      });\n      \n      \n      // emit(doc._id, {name: doc.name, code: doc.code, \"1月开盘\": m1.open, \"12月开盘\": m0.open, \"开盘价差\": parseFloat(m0.open - m1.open).toFixed(2), \"12月收盘\": m0.close,  \"收盘价差\": parseFloat(m0.close - m1.open).toFixed(2) });\n      \n      // for (var i =0 ; i < data.length; i++) {\n      //   var month = data[i]\n      // }\n      // emit(doc._id, 1);\n    }\n    \n  }\n}"
        },
        "jump": {
            "reduce": "_count",
            "map": "function (doc) {\n  var data = doc.data;\n  if(data.length == 9) {\n    \n    var m0 = data[data.length-1];\n    var m1 = data[data.length-2];\n    \n    var m2 = data[data.length-3];\n    var m3 = data[data.length-4];\n    \n    var m4 = data[data.length-5];\n    var m5 = data[data.length-6];\n    \n    var m6 = data[data.length-7];\n    var m7 = data[data.length-8];\n    // emit(doc._id, m2);\n    // var shiti = m1.close - m1.open > 0 ? m1.close : m1.open;\n    if (m1.open > m0.high) {\n      // emit(doc._id, m2);\n      \n      var buy = m1.dailyData[1].open;\n      \n      var diff1 = parseFloat(m1.close - buy).toFixed(2);\n      var diff1Ratio = parseFloat(diff1 / buy).toFixed(2);\n      \n      \n      var diff2 = parseFloat(m2.close - buy).toFixed(2);\n      var diff2Ratio = parseFloat(diff2 / buy).toFixed(2);\n      \n      \n      \n      var diff3 = parseFloat(m3.close - buy).toFixed(2);\n      var diff3Ratio = parseFloat(diff3 / buy).toFixed(2);\n      \n      \n      \n      var diff4 = parseFloat(m4.close - buy).toFixed(2);\n      var diff4Ratio = parseFloat(diff4 / buy).toFixed(2);\n      \n      \n      \n      var diff5 = parseFloat(m5.close - buy).toFixed(2);\n      var diff5Ratio = parseFloat(diff5 / buy).toFixed(2);\n      \n      \n      \n      var diff6 = parseFloat(m6.close - buy).toFixed(2);\n      var diff6Ratio = parseFloat(diff6 / buy).toFixed(2);\n      \n      \n      \n      var diff7 = parseFloat(m7.close - buy).toFixed(2);\n      var diff7Ratio = parseFloat(diff7 / buy).toFixed(2);\n      \n      \n      emit(doc._id, {name: doc.name, code: doc.code,\n      m1open: m1.open,\n      m12high: m12.high,\n      highDiff: parseFloat(m1.high - m2.open).toFixed(2),\n      \n      buy: buy,\n      \n      close1: m1.close,\n      diff1: diff1,\n      diff1Ratio: diff1Ratio,\n      \n      \n      close2: m2.close,\n      diff2: diff2,\n      diff2Ratio: diff2Ratio,\n      \n      \n      close3: m3.close,\n      diff3: diff3,\n      diff3Ratio: diff3Ratio,\n      \n      \n      close4: m4.close,\n      diff4: diff4,\n      diff4Ratio: diff4Ratio,\n      \n      \n      close5: m5.close,\n      diff5: diff5,\n      diff5Ratio: diff5Ratio,\n      \n      \n      close6: m6.close,\n      diff6: diff6,\n      diff6Ratio: diff6Ratio,\n      \n      \n      close7: m7.close,\n      diff7: diff7,\n      diff7Ratio: diff7Ratio,\n      \n      });\n      \n      // for (var i =0 ; i < data.length; i++) {\n      //   var month = data[i]\n      // }\n      // emit(doc._id, 1);\n    }\n    \n  }\n}"
        }
    },
    "language": "javascript"
}

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
db = None
try:
    db = couch.create('longterm_'+today)
except:
    db = couch['longterm_'+today]

# db = couch.create('longterm_'+today)
# db = couch['longterm_'+today]
stocks = ak.stock_zh_a_spot_em()


period="monthly"
# period="daily"
# period="weekly"



count=0

def saveStock(list):

    for stock in list:

        code=stock['code']
        name=stock['name']

        print("start to save stock ================================================" , code , name, end='\n * ')

        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period="monthly", start_date=startDate, end_date=today, adjust="qfq")
        # print(stock_zh_a_hist_df)
        global count
        count = count + 1
        print("count:  " , count, end='\n')
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
            try:
                db.save({'_id':  data[0]["date"] + '_' + code,
                        'date': data[0]["date"],
                        'name': name,
                        'code': code,
                        'data': data,
                        })
            except:
                print(f"{bcolors.FAIL} saving error xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx {code} {name} {bcolors.ENDC}", end='\n')



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

    if len(stockList) >= 50:
        t1 = threading.Thread(target=saveStock, args=(stockList,))
        t1.start()
        print("start thread =====================> " , sindex, end='\n')
        stockList=[]

if len(stockList) > 0:
    t1 = threading.Thread(target=saveStock, args=(stockList,))
    t1.start()
    print("start thread =====================> " , sindex, end='\n')
    stockList=[]

# 创建线程
# t1 = threading.Thread(target=saveStock, args=(1,))
# t2 = threading.Thread(target=saveStock, args=(2,))


print("............保存 Design View.............")

db.save(design_view)

print("............完成.............")

