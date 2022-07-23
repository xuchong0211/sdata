import akshare as ak
import couchdb
import pandas as pd
from datetime import date, timedelta
import numpy as np



today = date.today().strftime("%Y%m%d")
startDate = (date.today() + timedelta(weeks=-90)).strftime("%Y%m%d")

design_view = {
  "_id": "_design/g8",
  "views": {
    "mai1_3": {
      "reduce": "_count",
      "map": "function (doc) {\n  var week0 = doc.weeks[0];\n  \n  var week1 = doc.weeks[1];\n  \n  var week2 = doc.weeks[2];\n  \n  var week3 = doc.weeks[3];\n  \n  var ma10 = doc.m10;\n  var ma60 = doc.m60;\n  \n  var goldCross = false;\n  \n  var over = week0.close > ma60[0];\n  \n  var up = ma60[0] > ma60[1];\n  \n  var bigRed = false;\n  \n  for(var i=0; i < 3; i++) {\n    if(ma10[i] >= ma60[i] && ma10[i+1] < ma60[i+1]) {\n    // if(ma10[i] >= ma60[i]) {\n      goldCross = true;\n    }\n    \n    \n    if(doc.weeks[i].range >= 5 && doc.weeks[i].close > doc.weeks[i].open) {\n      bigRed = true;\n    }\n  }\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n    // emit([doc.date,doc.code,doc.name], {a: goldCross, b:bigRed, c:over});\n  \n  if (goldCross && bigRed && over && available && up) {\n    emit([doc.date,doc.code,doc.name],  {code: doc.code,name: doc.name, open: week0.open, close: week0.close});\n  }\n  \n  \n  \n}"
    },
    "mai2_3": {
      "map": "function (doc) {\n  var weeks = doc.weeks;\n  \n  var week0 = weeks[0];\n  \n  var week1 = weeks[1];\n  \n  var week2 = weeks[2];\n  \n  var week3 = weeks[3];\n  \n  var ma10 = doc.m10;\n  var ma60 = doc.m60;\n  \n  var stand = ma10[3] > ma60[3];\n  \n  var near = Math.abs((weeks[3].close - ma60[3])) / ma60[3];\n  \n  var over = week0.close > ma60[0];\n  \n  var up = true;\n  \n  var bigRed = false;\n  \n  for(var i=0; i < 3; i++) {\n    \n    var neari = (weeks[i].close - ma60[i]) / ma60[i];\n    \n    if (neari < near) {\n      near = neari;\n    }\n    \n    if(ma60[i] < ma60[i+1]) {\n      up = false;\n    }\n    \n    \n    // if(weeks[i].close < ma60[i]) {\n    //   over = false;\n    // }\n    \n    \n    \n    if(ma10[i] < ma60[i]) {\n      stand = false;\n    }\n    \n    if(weeks[i].close < ma60[i]) {\n      stand = false;\n    }\n    \n    \n    if(weeks[i].range >= 5 && weeks[i].close > weeks[i].open) {\n      bigRed = true;\n    }\n  }\n  \n  var available = true;\n  \n  if(doc.code.indexOf(\"688\") >= 0) {\n    available = false\n  }\n  \n  \n  if(doc.code.indexOf(\"300\") >= 0) {\n    available = false\n  }\n  \n  if(doc.name.indexOf(\"ST\") >= 0) {\n    available = false\n  }\n  \n    // emit([doc.date,doc.code,doc.name], {stand: stand, bigRed:bigRed, over:over, up:up});\n  \n  if (near < 0.03 && stand && bigRed && over && available && up) {\n    emit([doc.date,doc.code,doc.name],  {code: doc.code,name: doc.name, open: week0.open, close: week0.close, near: near});\n  }\n  \n  \n  \n}"
    }
  },
  "language": "javascript"
}

couch = couchdb.Server('http://admin:password@127.0.0.1:5984/')
db = couch.create('g8_'+today)
# db = couch['g8_']
stocks = ak.stock_zh_a_spot_em()


# period="monthly"
# period="daily"
period="weekly"


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

    # print("start.........: "+name)
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
        # print("count : " + str(count))
    # db.save({'_id':  today + '_' + code,
    #             'date': today,
    #             'name': name,
    #             'code': code,
    #             'data': data,
    #             })
    data.reverse()

    print("==================data======================="+str(len(data)))
    # print(data)

    ma10_0 = 0
    ma10_1 = 0
    ma10_2 = 0
    ma10_3 = 0

    ma60_0 = 0
    ma60_1 = 0
    ma60_2 = 0
    ma60_3 = 0

    weeks = []

    for i in range(len(data)) :

        if i < 30 :
            weeks.append(data[i])

        print("index=============================="+ str(i))
        if i < 60 :
            ma60_0 = ma60_0 + data[i]["close"]

        
        if i > 0 and i < 61 :
            ma60_1 = ma60_1 + data[i]["close"]

        
        if i > 1 and i < 62 :
            ma60_2 = ma60_2 + data[i]["close"]

        
        if i > 2 and i < 63 :
            ma60_3 = ma60_3 + data[i]["close"]
        
        print("index=============================="+ str(i))

        if i < 10 :
            ma10_0 = ma10_0 + data[i]["close"]

        
        if i > 0 and i < 11 :
            ma10_1 = ma10_1 + data[i]["close"]

        
        if i > 1 and i < 12 :
            ma10_2 = ma10_2 + data[i]["close"]

        
        if i > 2 and i < 13 :
            ma10_3 = ma10_3 + data[i]["close"]


    print("==========10============")
    print(round((ma10_0/10),3))
    print(round((ma10_1/10),3))
    print(round((ma10_2/10),3))
    print(round((ma10_3/10),3))

    print("==========60============")
    print(round((ma60_0/60),3))
    print(round((ma60_1/60),3))
    print(round((ma60_2/60),3))
    print(round((ma60_3/60),3))

    row = {
        '_id': today +"_"+code,
        'date': today,
        'name': name,
        'code': code,
        'weeks': weeks,
        'm10': [round((ma10_0/10),3),round((ma10_1/10),3),round((ma10_2/10),3),round((ma10_3/10),3)],
        'm60': [round((ma60_0/60),3),round((ma60_1/60),3),round((ma60_2/60),3),round((ma60_3/60),3)],
    }

    db.save(row)

print("............end.............")

