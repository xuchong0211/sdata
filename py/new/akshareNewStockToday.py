import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta
import numpy as np



today = date.today().strftime("%Y%m%d")
startDate = (date.today() + timedelta(days=-31)).strftime("%Y%m%d")

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
# db = couch.create('test')
db = couch['stock_new_month']
new_stocks = ak.stock_zh_a_new_em()


# period="monthly"
period="daily"
# period="weekly"

# todayStr = date.today().strftime("%Y-%m-%d")
todayStr = "2022-07-22"

for index, row in new_stocks.iterrows():

# 序号	int64	-
# 代码	object	- 1
# 名称	object	- 2
# 最新价	float64	- 3
# 涨跌幅	float64	注意单位: % 4
# 涨跌额	float64	- 5
# 成交量	float64	- 6
# 成交额	float64	- 7
# 振幅	float64	注意单位: % 8
# 最高	float64	- 9
# 最低	float64	- 10
# 今开	float64	- 11
# 昨收	float64	- 12
# 量比	float64	- 13
# 换手率	float64	注意单位: % 14
# 市盈率-动态	float64	-
# 市净率	float64	-
    print(row)
    code = row[1]
    name = row[2]
    # name = row[3]
    # name = row[4]
    # name = row[5]
    # name = row[6]
    # name = row[7]
    # name = row[8]
    # name = row[9]
    # name = row[10]
    # open = row[11]
    # preCLose = row[12]
    # preCLose = row[13]
    # preCLose = row[14]
    print("start.........: "+name+code)
    

    db.save({'_id':  todayStr + '_' + code,
        'name': name,
        'code': code,
        'date': todayStr,
        'open': row[11],
        'close': row[3],
        'high': row[9],
        'low': row[10],
        'volume': row[6],
        'turn': row[7],
        'zhenfu': row[8],
        'range': row[4],
        'amount': row[5],
        'turnover': row[14],
        })
print("............end.........")


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
