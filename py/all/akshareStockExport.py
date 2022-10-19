import requests
import pandas as pd
import codecs
import json
from datetime import date, timedelta
import numpy as np
from xlwt import Workbook
import xlwt

def getName(name) :

    if name == "dayou":
      return "大有"

    elif name == "diao":
      return "一箭双雕"

    elif name == "doublelong":
      return "双龙取水"

    elif name == "fankeweizhuplus":
      return "反客为主plus"

    elif name == "feilong":
      return "飞龙在天"

    elif name == "gesandaniu":
      return "隔山打牛" 

    elif name == "gesandaniuplus" :
      return "隔山打牛plus"

    elif name == "jianlongplus":
      return "见龙plus"

    elif name == "shenlong3":
      return "神龙摆尾3"

    elif name == "shenlong1":
      return "神龙摆尾"

    elif name == "shenqijunxian":
      return "神奇均线"

    elif name == "yiyidailao":
      return "以逸待劳"

    elif name == "vmodel":
      return "V型反转"


today = date.today().strftime("%Y%m%d")
# today = "20220729"

urls =[
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/dayou",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/diao",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/doublelong",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/fankeweizhuplus",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/feilong",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniu",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniuplus",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/jianlongplus",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenlong3",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenlong1",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenqijunxian",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/yiyidailao",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/vmodel",
      ]

def getHeader ():
    return [
        '日期',
        '代码',
        '名称',
        '开盘价',
        '收盘价',
        '最高价',
        '底高价',
        ]

def formatData(data):
    list = []
    list.append(getHeader())
    print(data)
    if len(data) > 0:
        for item in data:
            date = item['key'][0]
            code = item['key'][1]
            # code = item['value']['code']
            name = item['value']['name']
            open = item['value']['open']
            close = item['value']['close']
            list.append([date, code, name, open, close])
    return list

def insertData(sheet, data) :
    # print(data)
    for row, rowData in enumerate(data):
        print(row, end="\n")
        for col, item in enumerate(rowData):
            sheet.col(col).width = 256*20
            sheet.write(row, col, item)

book = Workbook()

for url in urls:
    print(url)
    urlstr= url.split('/')
    mode = urlstr[len(urlstr)-1]
    print(mode)

    res = requests.get(url)

    data = res.json()
    data = data["rows"]

    sheet = book.add_sheet(getName(mode))
    data = formatData(data)
    insertData(sheet, data)

book.save(today+'_ExcelExport.xls')


# urls = url.split('/')
# mode = urls[len(urls)-1]


print("............end.........")
