import requests
import pandas as pd
import codecs
import json
from datetime import date, timedelta
import numpy as np
from xlwt import Workbook
import xlwt


def insertData(sheet, data) :
    # print(data)
    for row, rowData in enumerate(data):
        # print(row, end="\n")
        for col, item in enumerate(rowData):
            sheet.col(col).width = 256*120
            sheet.col(col).height = 80
            sheet.write(row, col, item)

print("=========================== start ===================================")
book = Workbook(style_compression=10)



# url ="http://127.0.0.1:5984/i18n/_design/i18n/_view/list"
# url ="http://127.0.0.1:5984/new_protocol/_design/list/_view/name?reduce=false"
# url ="http://127.0.0.1:5984/new_protocol1/_design/list/_view/riskFactor?reduce=false"
# url ="http://127.0.0.1:5984/new_protocol1/_design/list/_view/treatment?reduce=false"
# url ="http://127.0.0.1:5984/new_protocol1/_design/data/_view/symptoms"
url ="https://cdb.indorhcare.com/medications/_design/medication_doc/_view/name?include_docs=false"
res = requests.get(url)
data = res.json()
data_list = [["ID", "Name", "Indonesian", "category_en", "category_indo", "type", "unit", "quantity", "code", "dosage", "description"]]

for item in data['rows']:

    value = item['value']

    # print("item", item)
    # key = str(item['key'])
    # id = str(item['key'][0])
    # en = str(item['key'][1])
    # indo = str(item['key'][2])
    id = str(value['id'])
    name = str(value['en'])
    indo = str(value['indo'])
    category_en = "" if value.get('category_en') is None else str(value.get('category_en'))
    category_indo = "" if value.get('category_indo') is None else str(value.get('category_indo'))
    type = "" if value.get('type') is None else str(value.get('type'))
    quantity = "" if value.get('quantity') is None else str(value.get('quantity'))
    code = "" if value.get('code') is None else str(value.get('code'))
    dosage = "" if value.get('dosage') is None else str(value.get('dosage'))
    description = "" if value.get('description') is None else str(value.get('description'))

    data_list.append([id,
                      name,
                      indo,
                      category_en,
                      category_indo,
                      type,
                      quantity,
                      code,
                      dosage,
                      description
                      ])

print("data list========================================-------------------------======");
print( data_list);

sheet = book.add_sheet('madications')
insertData(sheet, data_list)


# url ="http://127.0.0.1:5984/new_protocol/_design/list/_view/description?group=true"
# res = requests.get(url)
# data = res.json()
# data_list = []
#
# for item in data['rows']:
#
#     id = str(item['key'][0])
#     en = str(item['key'][1])
#     indo = str(item['key'][2])
#
#     data_list.append([id, en,indo])
#
# print("data list", data);
#
# sheet = book.add_sheet('description')
# insertData(sheet, data_list)
#
#
#
#
# url ="http://127.0.0.1:5984/new_protocol/_design/list/_view/complaint?group=true&gourp_level=1"
# res = requests.get(url)
# data = res.json()
# data_list = []
#
# for item in data['rows']:
#
#     en = str(item['key'][0])
#     indo = str(item['key'][1])
#     # s = {'en': en, 'indo': indo}
#
#     data_list.append([en,indo])
#
# print("data list", data);
#
# sheet = book.add_sheet('symptoms')
# insertData(sheet, data_list)
#
#
# url ="http://127.0.0.1:5984/new_protocol/_design/list/_view/riskFactor?group=true"
# res = requests.get(url)
# data = res.json()
# data_list = []
#
# for item in data['rows']:
#
#     en = str(item['key'][0])
#     indo = str(item['key'][1])
#     # s = {'en': en, 'indo': indo}
#
#     data_list.append([en,indo])
#
# print("data list", data);
#
# sheet = book.add_sheet('riskFactor')
# insertData(sheet, data_list)
#
#
#
# url ="http://127.0.0.1:5984/new_protocol/_design/list/_view/physicalExamination?group=true"
# res = requests.get(url)
# data = res.json()
# data_list = []
#
# for item in data['rows']:
#
#     en = str(item['key'][0])
#     indo = str(item['key'][1])
#     # s = {'en': en, 'indo': indo}
#
#     data_list.append([en,indo])
#
# print("data list", data);
#
# sheet = book.add_sheet('physicalExamination')
# insertData(sheet, data_list)
#
#
#
#
# url ="http://127.0.0.1:5984/new_protocol/_design/list/_view/supportingExamination?group=true"
# res = requests.get(url)
# data = res.json()
# data_list = []
#
# for item in data['rows']:
#
#     en = str(item['key'][0])
#     indo = str(item['key'][1])
#     # s = {'en': en, 'indo': indo}
#
#     data_list.append([en,indo])
#
# print("data list", data);
#
# sheet = book.add_sheet('supportingExamination')
# insertData(sheet, data_list)







book.save('medications20230821.xls')

