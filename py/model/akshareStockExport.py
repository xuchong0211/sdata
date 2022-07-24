import requests
import pandas as pd
from datetime import date, timedelta
import numpy as np


design_view = {
  "_id": "_design/list",
  "views": {
    "diao": {
      "map": "function (doc) {\n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var small1 = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var small2 = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var small3 = day3.open > day3.close && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n      \n      var small4 = day4.open < day4.close && Math.abs(day4.open - day4.close)/day4.open > 0.04;\n      \n      var gaokai = day3.open > day4.close || day2.open > day3.close;\n      //emit([doc.date, doc.code], {name: doc.name});\n      if (small1 && small2 && small3 && small4) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    },
    "feilong": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var overall =  day1.close > day1.open && day1.close > day2.close && day1.close > day3.close && day1.close > day4.close;\n      \n      //var small2 = day2.open < day2.close;// && Math.abs(day2.open - day2.close)/day2.open > 0.005;\n      var smallSolid =  Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var gaokai = day2.open > day3.close;\n      \n      var tiaokong = day2.low > day3.high;\n      \n      var zhangting = day3.range > 9.96;\n     \n      if (overall && smallSolid && zhangting && gaokai && tiaokong) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "jianlong": {
      "map": "function (doc) {\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var overall = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n      \n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var smallSolid = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var gaokai = day2.open > day3.close;\n      \n      var stand = day4.open < day1.low && day4.open < day2.low && day4.open < day3.low;\n      \n      //A\n      var day3Red = day3.open < day3.close;// && Math.abs(day3.open - day3.close)/day3.open < 0.03;\n      \n      //B\n      var day3Green = day3.open > day3.close && Math.abs(day3.open - day3.close)/day2.open < 0.03;\n      \n      \n      if (overall && smallSolid && gaokai && stand && (day3Red || day3Green)) {\n        emit([doc.date, doc.code], {name: doc.name, code: doc.code, open: day1.open, close: day1.close });\n      }\n    }\n  }\n}"
    },
    "flower": {
      "map": "function (doc) {\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      //emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var solid = Math.abs(day1.open - day1.close)/day1.open > 0.01;\n      \n      var smallSolid = Math.abs(day2.open - day2.close)/day2.open <= 0.005;\n      \n      var threeGao = day1.close > day2.close && day1.high > day2.high && day1.low > day2.low;\n      \n      var stand = day3.low < day2.low;\n      \n      if (solid && smallSolid && threeGao && stand) {\n        emit([doc.date, doc.code], {code: doc.code, name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    },
    "doublelong": {
      "map": "function (doc) {\n  \n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    \n    var data = doc.data;\n    if (data && data.length > 7) {\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      \n      var volume = day2.volume > day3.volume && day2.volume > day1.volume;\n      \n      var zhangting = day1.range > 9.96 && day2.range > 9.96;\n     \n      if (zhangting && volume) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n  \n}"
    },
    "dayou": {
      "map": "function (doc) {\n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n  if (available) {\n    var data = doc.data;\n    // emit([doc.date, doc.code], {name: doc.name});\n    if (data && data.length > 7) {\n      // emit([doc.date, doc.code], {name: doc.name});\n      var day1 = data[0];\n      var day2 = data[1];\n      var day3 = data[2];\n      var day4 = data[3];\n      var day5 = data[4];\n      var day6 = data[5];\n      \n      var overall = day1.open < day1.close && day1.close > day2.close && day1.close > day2.open && day1.close > day3.open && day1.close > day3.close && day1.close > day4.close;\n      \n      // emit([doc.date, doc.code], {name: doc.name});\n      var small2 = day2.open > day2.close && Math.abs(day2.open - day2.close)/day2.open < 0.03;\n      \n      var red = day4.open < day4.close && day3.open < day3.close && day3.open < day3.close;\n      \n      var gaokai = day3.open > day4.close || day2.open > day3.close;\n      //emit([doc.date, doc.code], {name: doc.name});\n      if (overall && small2 && red && small4 && small5) {\n        emit([doc.date, doc.code], {name: doc.name, open: day1.open, close: day1.close});\n      }\n    }\n  }\n  \n  \n}"
    }
  },
  "language": "javascript"
}

today = date.today().strftime("%Y%m%d")

# http://127.0.0.1:5984/stock_daily/_design/list/_view/flower?reduce=false&startkey=[%2220220719%22,%20%22%22]&&endkey=[%2220220719%22,%20%22SSSSSSSSSSSSSSSS%22]
url ="http://admin:password@127.0.0.1:5984/daily"+today+"/_design/diao/_view/list?reduce=false&startkey=[%2220220720%22,%20%22%22]&&endkey=[%2220220720%22,%20%22SSSSSSSSSSSSSSSS%22]"

res = requests.get(url)

data = res.json()
# print(data["rows"][0])


# print(data["rows"][0]['key'][0])

today = 20220720
# period="monthly"
period="daily"
# period="weekly"

print("=========================== start ===================================")


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

    date = item['key'][0]
    code = item['key'][1]
    name = item['value']['name']
    open = item['value']['open']
    close = item['value']['close']
    s = {'日期': date, '代码': ""+code+"", '名称': name, '开盘价': open, '收盘价':close,'模型': "一箭双雕（预选）"}

    data_list.append(s)
    # j = srow[1]

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

print(data_list)

result = pd.DataFrame(data_list, columns=['日期', '代码', '名称', '开盘价', '收盘价', '模型'])
result.to_csv("c:/2022_07_19_diao.csv", encoding="gbk", index=True)

print("............end.........")


