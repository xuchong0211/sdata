import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta
import numpy as np



today = date.today().strftime("%Y%m%d")
startDate = (date.today() + timedelta(days=-15)).strftime("%Y%m%d")

# couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
# db = couch.create('daily_'+today)


# stock_changes_em_df = ak.stock_changes_em(symbol="竞价上涨")
# print(stock_changes_em_df)
print("1111111111111111111111111")


stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol='sz002654')
print("22222222222222222222")
print(stock_zh_a_tick_tx_js_df)
#
# stocks = ak.stock_zh_a_spot_em()



period="daily"
# period="weekly"
# period="monthly"

count=0

# for index, srow in stocks.iterrows():
#
# # 名称	类型	描述
# # 序号	int64	-
# # 代码	object	-
# # 名称	object	-
# # 最新价	float64	-
# # 涨跌幅	float64	注意单位: %
# # 涨跌额	float64	-
# # 成交量	float64	注意单位: 手
# # 成交额	float64	注意单位: 元
# # 振幅	float64	注意单位: %
# # 最高	float64	-
# # 最低	float64	-
# # 今开	float64	-
# # 昨收	float64	-
# # 量比	float64	-
# # 换手率	float64	注意单位: %
# # 市盈率-动态	float64	-
# # 市净率	float64	-
# # 总市值	float64	注意单位: 元
# # 流通市值	float64	注意单位: 元
# # 涨速	float64	-
# # 5分钟涨跌	float64	注意单位: %
# # 60日涨跌幅	float64	注意单位: %
# # 年初至今涨跌幅	float64	注意单位: %
#     code = srow[1]
#     name = srow[2]
#     print("start.........: ", code, name)
#     stock_zh_a_tick_tx_df = ak.stock_zh_a_tick_tx(symbol='sz002654', trade_date=today)
#     print(stock_zh_a_tick_tx_df)
#
#     count = count + 1
#
#     data=[]
#

# db.save(design_view)

# print("............模型导入完成...........")


print("............结束...........")
