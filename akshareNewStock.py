import akshare as ak
import couchdb
import pandas as pd

# couch = couchdb.Server('http://localhost:5984/')
# db = couch.create('test')
# db = couch['astock']
stock_zh_a_new_df = ak.stock_zh_a_new()
# for c in stock_zh_a_hist_df
# data_df = pd.DataFrame()
#



# data_df = pd.DataFrame()
# for code in stock_df["code"]:
#     print("Downloading :" + code)
#     k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
#     data_df = data_df.append(k_rs.get_data())
# bs.logout()
# data_df.to_csv("~/20200610.DayData.csv", encoding="gbk", index=False)


# for index, row in stock_zh_a_new_df.iterrows():
# #     result = db.save(row)

#     data_df = data_df.append({'date': row[0],
#     'code': row[1],
#     'name': row[2],
#     })
    # print({'date': row[0],
    # 'code': row[1],
    # 'name': row[2],
    # })
#     data_df = data_df.append(code)
stock_zh_a_new_df.to_csv("c:/20200610.new.csv", encoding="gbk", index=False)
# print(stock_zh_a_hist_df[0:5])

# stock_zh_a_hist_df.to_csv("~/20200610.DayData.csv", encoding="gbk", index=False)

# doc = {'foo': 'stock_zh_a_hist_df'}
# result = db.save(doc)
# print(result)
