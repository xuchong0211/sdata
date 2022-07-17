import akshare as ak
import couchdb
import pandas as pd

couch = couchdb.Server('http://localhost:5984/')
# db = couch.create('test')
db = couch['astock']
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20220301", end_date='20220707', adjust="qfq")
# for c in stock_zh_a_hist_df
# data_df = pd.DataFrame()
#
for index, row in stock_zh_a_hist_df.iterrows():
#     result = db.save(row)
    db.save({'date': row[0],
              'close': row[1],
              'high': row[2],
              'low': row[3],
              'open': row[4],
              'volume': row[5],
              'outstanding_share': row[6],
              'turnover': row[7],
              })
#     data_df = data_df.append(code)

# print(stock_zh_a_hist_df[0:5])

# stock_zh_a_hist_df.to_csv("~/20200610.DayData.csv", encoding="gbk", index=False)

# doc = {'foo': 'stock_zh_a_hist_df'}
# result = db.save(doc)
# print(result)
