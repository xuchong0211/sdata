import akshare as ak
import couchdb
import pandas as pd

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
# db = couch.create('test')
db = couch['stock_new_month']
stock_zh_a_new_df = ak.stock_zh_a_new_em()


# period="monthly"
period="daily"
# period="weekly"


for index, srow in stock_zh_a_new_df.iterrows():

# 序号	int64	-
# 代码	object	-
# 名称	object	-
# 最新价	float64	-
# 涨跌幅	float64	注意单位: %
# 涨跌额	float64	-
# 成交量	float64	-
# 成交额	float64	-
# 振幅	float64	注意单位: %
# 最高	float64	-
# 最低	float64	-
# 今开	float64	-
# 昨收	float64	-
# 量比	float64	-
# 换手率	float64	注意单位: %
# 市盈率-动态	float64	-
# 市净率	float64	-
    code = srow[1]
    name = srow[2]
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period=period, start_date="20220701", end_date='20220718', adjust="qfq")
# print(stock_zh_a_hist_df)

    print("start.........: "+name)
#
    for index, row in stock_zh_a_hist_df.iterrows():
    #     result = db.save(row)

# 日期	object	交易日
# 开盘	float64	开盘价
# 收盘	float64	收盘价
# 最高	float64	最高价
# 最低	float64	最低价
# 成交量	int32	注意单位: 手
# 成交额	float64	注意单位: 元
# 振幅	float64	注意单位: %
# 涨跌幅	float64	注意单位: %
# 涨跌额	float64	注意单位: 元
# 换手率	float64	注意单位: %
        db.save({'_id':  row[0] + '_' + code,
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
