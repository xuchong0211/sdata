import requests
import pandas as pd
import codecs
import json
from datetime import date, timedelta
import numpy as np


ipAddress = "127.0.0.1:5984"


today = date.today().strftime("%Y%m%d")
# today = "20220729"

url ="http://admin:password@"+ipAddress+"/g8_"+today+"/_design/g8/_view/mai1_3?reduce=false"


urls = url.split('/')
mode = urls[len(urls)-1]

res = requests.get(url)

data = res.json()


print("=========================== start ===================================" + today)


data_list = []

for item in data['rows']:

    date = item['key'][0]
    code = str(item['key'][1])
    name = item['key'][2]
    open = item['value']['open']
    close = item['value']['close']
    s = {'代码': "_"+code, '名称': name, '开盘价': open, '收盘价': close}

    data_list.append(s)


print(data_list)

result = pd.DataFrame(data_list, columns=['代码', '名称', '开盘价', '收盘价'])
result[["代码"]] = result[["代码"]].astype('string')
result.to_csv("./"+date + "_g8_mai_1_3_stock.csv", encoding="gbk", index=False)

url ="http://admin:password@"+ipAddress+"/g8_"+today+"/_design/g8/_view/mai2_3?reduce=false"

res = requests.get(url)

data = res.json()


print("=========================== start ===================================")


data_list = []

for item in data['rows']:

    date = item['key'][0]
    code = str(item['key'][1])
    name = item['key'][2]
    open = item['value']['open']
    close = item['value']['close']
    s = {'代码': "_"+code, '名称': name, '开盘价': open, '收盘价': close}

    data_list.append(s)


print(data_list)

result = pd.DataFrame(data_list, columns=['代码', '名称', '开盘价', '收盘价'])
result[["代码"]] = result[["代码"]].astype('string')
result.to_csv("./"+date + "_g8_mai_2_3_stock.csv", encoding="gbk", index=False)

# with codecs.open("~/"+date + "_g8_mai_1_3_stock.txt", 'w', 'utf-8') as f:
#  f.write(result.to_string())

print("............end.........")
