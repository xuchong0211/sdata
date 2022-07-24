import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta
import numpy as np



today = date.today().strftime("%Y%m%d")
startDate = (date.today() + timedelta(days=-15)).strftime("%Y%m%d")

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
db = couch.create('daily_'+today)
stocks = ak.stock_zh_a_spot_em()



period="daily"
# period="weekly"
# period="monthly"

count=0

for index, srow in stocks.iterrows():

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
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period=period, start_date=startDate, end_date=today, adjust="qfq")
# print(stock_zh_a_hist_df)

    print("start.........: "+name)
    count = count + 1

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
    print(count)

    if len(data) > 0 :
        data.reverse()
        db.save({'_id':  data[0]["date"] + '_' + code,
                'date': data[0]["date"],
                'name': name,
                'code': code,
                'data': data,
                })
print(count)
print("............end...........")


# http://127.0.0.1:5984/stock_new_month/_design/name/_view/price?gourp=true&group_level=2
# http://127.0.0.1:5984/stock_new_month/_design/name/_view/p?gourp=true&group_level=0
# http://127.0.0.1:5984/stock_new_month/_design/name/_view/list?gourp=true&group_level=1


# {
#   "_id": "_design/name",
#   "_rev": "16-90546b50788f1aac19a007e8eb79765b",
#   "views": {
#     "list": {
#       "map": "function (doc) {\n  emit([doc.code, doc.name], {name: doc.name, code: doc.code});\n}",
#       "reduce": "_count"
#     },
#     "price": {
#       "reduce": "_stats",
#       "map": "function (doc) {\n  emit([doc.code, doc.name], doc.close);\n}"
#     },
#     "p": {
#       "reduce": "_approx_count_distinct",
#       "map": "function (doc) {\n  emit([doc.code, doc.name], doc.close);\n}"
#     }
#   },
#   "language": "javascript"
# }





# {
#   "_id": "_design/list",
#   "_rev": "26-6048a5984093e233b20e569b6fc4b367",
#   "views": {
#     "diao": {
#       "map": "function (doc) {\n  var data = doc.data;\n  // emit([doc.date, doc.code], {name: doc.name});\n  if (data && data.length > 7) {\n    // emit([doc.date, doc.code], {name: doc.name});\n    var day1 = data[data.length-1];\n    var day2 = data[data.length-2];\n    var day3 = data[data.length-3];\n    var day4 = data[data.length-4];\n    \n    var small1 = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n    \n    // emit([doc.date, doc.code], {name: doc.name});\n    var small2 = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n    \n    var small3 = day3.open > day3.close && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n    \n    var small4 = day4.open < day4.close && Math.abs(day4.open - day4.close)/day4.open > 0.04;\n    //emit([doc.date, doc.code], {name: doc.name});\n    if (small1 && small2 && small3 && small4) {\n      emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n    }\n    // emit([doc.date, doc.code], {name: doc.name});\n  }\n  \n  \n}"
#     },
#     "jianlongA": {
#       "map": "function (doc) {\n  var data = doc.data;\n  // emit([doc.date, doc.code], {name: doc.name});\n  if (data && data.length > 7) {\n    // emit([doc.date, doc.code], {name: doc.name});\n    var day1 = data[data.length-1];\n    var day2 = data[data.length-2];\n    var day3 = data[data.length-3];\n    var day4 = data[data.length-4];\n    \n    var small1 = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n    \n    \n    // emit([doc.date, doc.code], {name: doc.name});\n    var small2 = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n    \n    var gao = day2.open > day3.close;\n    \n    var small3 = day3.open < day3.close;// && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n    \n    //var small4 = day4.open < day4.close && Math.abs(day4.open - day4.close)/day4.open > 0.04;\n    //emit([doc.date, doc.code], {name: doc.name});\n    if (small1 && small2 && small3 && gao) {\n      if(!(doc.code.indexOf(\"688\") >= 0 || doc.code.indexOf(\"300\") >= 0)) {\n        emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: day1.open, close: day1.close });\n      }\n      // emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n    }\n    // emit([doc.date, doc.code], {name: doc.name});\n  }\n  \n  \n}"
#     },
#     "feilong": {
#       "map": "function (doc) {\n  var data = doc.data;\n  // emit([doc.date, doc.code], {name: doc.name});\n  if (data && data.length > 7) {\n    // emit([doc.date, doc.code], {name: doc.name});\n    var day1 = data[data.length-1];\n    var day2 = data[data.length-2];\n    var day3 = data[data.length-3];\n    var day4 = data[data.length-4];\n    \n    var small1 = day1.open < day1.close && day1.close > day2.close && day1.close > day3.close && day1.close > day4.close;\n    \n    // emit([doc.date, doc.code], {name: doc.name});\n    //var small2 = day2.open < day2.close;// && Math.abs(day2.open - day2.close)/day2.open > 0.005;\n    var small2 =  Math.abs(day2.open - day2.close)/day2.open < 0.03;\n    \n    var gao = day2.open > day3.close;\n    \n    var kong = day2.low > day3.high;\n    \n    //var small3 = day3.open < day3.close && day3.close == day3.high && Math.abs(day4.close - day3.close)/day4.close > 0.098;\n    var small3 = day3.range > 9.96;\n   \n    //var small4 = day4.open < day4.close && Math.abs(day4.open - day4.close)/day4.open > 0.04;\n    //emit([doc.date, doc.code], {name: doc.name});\n    if (small1 && small2 && small3 && gao && kong) {\n    // if (small3) {\n      emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n    }\n    // emit([doc.date, doc.code], {name: doc.name});\n  }\n  \n  \n}"
#     }
#   },
#   "language": "javascript"
# }