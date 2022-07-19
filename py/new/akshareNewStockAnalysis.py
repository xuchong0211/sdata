import requests
import akshare as ak
import pandas as pd

url ="http://admin:password@127.0.0.1:5984/stock_new_month/_design/name/_view/price?gourp=true&group_level=2"

res = requests.get(url)

data = res.json()
# print(data["rows"][0])


# print(data["rows"][0]['key'][0])


# period="monthly"
period="daily"
# period="weekly"

print("=========================== start ===================================")

today = "20220719"
data_list = []

for item in data['rows']:

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

    code = item['key'][0]
    name = item['key'][1]
    max = item['value']['max']
    min = item['value']['min']
    level = max * 0.35
    # s = {'代码': ""+code+"", '名称': name, '最高价': max, '最低价': min, '35': level}
    print("start================================: "+ name);
    # data_list.append(s)

    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period=period, start_date=today, end_date=today, adjust="qfq")
# print(stock_zh_a_hist_df)

#     print("start.........: "+name)
# #
    for index, row in stock_zh_a_hist_df.iterrows():
        close = row[2]
        if close <= level and close >= min:
            data_list.append({'日期': today, '代码': ""+code+"", '名称': name, '最高价': max, '最低价': min, '35%': level, '收盘价': close})
            print("合适 =======================================:" + name)
        else :
            print("不合适 ....................................:" + name)

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

print(data_list)

result = pd.DataFrame(data_list, columns=['日期', '代码', '名称', '最高价','最低价','35%','收盘价'])
result.to_csv("~/2022_07_18_new_stock_33.csv", encoding="gbk", index=True)

print("............end.........")
