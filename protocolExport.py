import requests
import pandas as pd
import codecs
import json
from datetime import date, timedelta
import numpy as np
from xlwt import Workbook
import xlwt


urls =[
    "http://127.0.0.1:5984/symptoms/_design/list/_view/complaint?group=true&gourp_level=0",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/diao",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/doublelong",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/fankeweizhuplus",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/feilong",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniu",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniuplus",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/jianlongplus",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenlong3",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenlong1",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenqijunxian",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/yiyidailao",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/vmodel",
      ]
urls1 =[
    "http://127.0.0.1:5984/symptoms/_design/list/_view/complaint?reduce=false",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/diao",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/doublelong",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/fankeweizhuplus",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/feilong",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniu",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniuplus",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/jianlongplus",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenlong3",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenlong1",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenqijunxian",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/yiyidailao",
    # "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/vmodel",
      ]

def getHeader ():
    return [
        'symptom',
        'number',
        ]
def getHeader1 ():
    return [
        'symptom',
        'protocol',
        ]

def formatData(data):
    list = []
    list.append(getHeader())
    print(data)
    if len(data) > 0:
        for item in data:
            symptom = item['key'][0]
            # code = item['value']['code']
            number = item['value']
            # open = item['value']['open']
            # close = item['value']['close']
            list.append([symptom, number])
    return list

def formatData1(data):
    list = []
    list.append(getHeader1())
    print(data)
    if len(data) > 0:
        for item in data:
            symptom = item['key'][0]
            # code = item['value']['code']
            number = item['value']
            # open = item['value']['open']
            # close = item['value']['close']
            list.append([symptom, number])
    return list

def insertData(sheet, data) :
    # print(data)
    for row, rowData in enumerate(data):
        print(row, end="\n")
        for col, item in enumerate(rowData):
            sheet.col(col).width = 256*20
            sheet.write(row, col, item)

book = Workbook()


dataList = []

category = True
# category = False

for url in urls:
    print(url)
    mode = 'symptoms'
    # if idx == 0:
    #     max = 'symptoms'
    # else:
    #     mode = 'protocol'

    print(mode)

    res = requests.get(url)

    data = res.json()
    data = data["rows"]

    data = formatData(data)

    sheet = book.add_sheet(mode)
    insertData(sheet, data)

for url in urls1:
    print(url)
    mode = 'protocol'
    # if idx == 0:
    #     max = 'symptoms'
    # else:
    #     mode = 'protocol'

    print(mode)

    res = requests.get(url)

    data = res.json()
    data = data["rows"]

    data = formatData1(data)

    sheet = book.add_sheet(mode)
    insertData(sheet, data)

book.save('./all_symptoms.xls')


# urls = url.split('/')
# mode = urls[len(urls)-1]


print("............end.........")
