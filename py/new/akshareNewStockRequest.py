import requests  
import json

url ="http://admin:password@127.0.0.1:5984/stock_new_month/_design/name/_view/price?gourp=true&group_level=2"

res = requests.get(url)

data = res.json()
print(data["rows"][0])


print(data["rows"][0]['key'][0])


# period="monthly"
period="daily"
# period="weekly"


for index, srow in data['rows']:
    
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
    # print(index)
    
    # print(srow)
    j = srow[1]

    # print(j)
    # code = srow.key[0]
    # max = srow.value.max
    # print(code + ".........: "+max)
    # stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period=period, start_date="20220701", end_date='20220717', adjust="qfq")
# print(stock_zh_a_hist_df)

#     print("start.........: "+name)
# #
#     for index, row in stock_zh_a_hist_df.iterrows():
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
        # db.save({'_id':  row[0] + '_' + code,
        #     'name': name,
        #     'code': code,
        #     'date': row[0],
        #     'open': row[1],
        #     'close': row[2],
        #     'high': row[3],
        #     'low': row[4],
        #     'volume': row[5],
        #     'turn': row[6],
        #     'range': row[7],
        #     'amount': row[8],
        #     'turnover': row[9],
        #     })
print("............end.........")
