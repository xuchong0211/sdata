import requests
import pandas as pd
from xlwt import Workbook
import xlwt
import codecs
import json
from datetime import date, timedelta
import numpy as np



# today = date.today().strftime("%Y%m%d")
today = "20220729"

# url ="http://admin:password@127.0.0.1:5984/g8_"+today+"/_design/g8/_view/mai1_3?reduce=false"
url ="http://admin:password@127.0.0.1:5984/longterm_20220810/_design/months/_view/over"


# urls = url.split('/')
# mode = urls[len(urls)-1]

res = requests.get(url)

data = res.json()


print("=========================== start ===================================")
def formatData(data, header):
    list = []
    list.append(header)
    for item in data:
        row = []
        for key in item:
            row.append(item[key])
        list.append(row)
    return list

def getHeader (i):
    return ['代码',
          '名称',
          '1月开盘价',
          '12月开盘价',
          '开盘价差',
          '12月收盘价',
          '收盘价差',
          '买点',
          '1月收盘价',
          '1月盈利',
          '1月盈利百分比',
          str(i) + '月收盘价',
          str(i) + '月盈利',
          str(i) + '月盈利百分比',
          ]

def insertData(sheet, data) :
# print(data)

    for row, rowData in enumerate(data):
        print(row, end="\n")
        for col, item in enumerate(rowData):
            if row == 0 :
                sheet.write(row, col, item)

            elif row > 0 :
                # if col == 4 or col == 6 or col == 9 or col == 10 or col == 12 or col == 13 :
                if col == 4:
                    st = xlwt.easyxf('pattern: pattern solid;')
                    st.pattern.pattern_fore_colour = 3
                    sheet.write(row, col, item, st)
                elif col == 6:
                    st = xlwt.easyxf('pattern: pattern solid;')
                    st.pattern.pattern_fore_colour = 3
                    sheet.write(row, col, item, st)
                elif col == 9:
                    st = xlwt.easyxf('pattern: pattern solid;')
                    st.pattern.pattern_fore_colour = 3
                    sheet.write(row, col, item, st)
                elif col == 10:
                    st = xlwt.easyxf('pattern: pattern solid;')
                    st.pattern.pattern_fore_colour = 2
                    sheet.write(row, col, item, st)
                elif col == 12:
                    st = xlwt.easyxf('pattern: pattern solid;')
                    st.pattern.pattern_fore_colour = 2
                    sheet.write(row, col, item, st)
                elif col == 13:
                    st = xlwt.easyxf('pattern: pattern solid;')
                    st.pattern.pattern_fore_colour = 3
                    sheet.write(row, col, item, st)
                else :
                    sheet.write(row, col, item)
                # sheet.write(row, col, item)


data_list1 = []
data_list2 = []
data_list3 = []
data_list4 = []
data_list5 = []
data_list6 = []
data_list7 = []

for item in data['rows']:

    print(item)

    date = item['key']
    code = item['value']['code']
    name = item['value']['name']
    m1open = item['value']['m1open']
    m12open = item['value']['m12open']
    openDiff = item['value']['openDiff']
    m12close = item['value']['m12close']
    closeDiff = item['value']['closeDiff']


    buy = item['value']['buy']

    close1 = item['value']['close1']
    diff1 = item['value']['diff1']
    diff1Ratio = item['value']['diff1Ratio']


    close2 = item['value']['close2']
    diff2 = item['value']['diff2']
    diff2Ratio = item['value']['diff2Ratio']


    close3 = item['value']['close3']
    diff3 = item['value']['diff3']
    diff3Ratio = item['value']['diff3Ratio']


    close4 = item['value']['close4']
    diff4 = item['value']['diff4']
    diff4Ratio = item['value']['diff4Ratio']


    close5 = item['value']['close5']
    diff5 = item['value']['diff5']
    diff5Ratio = item['value']['diff5Ratio']


    close6 = item['value']['close6']
    diff6 = item['value']['diff6']
    diff6Ratio = item['value']['diff6Ratio']


    close7 = item['value']['close7']
    diff7 = item['value']['diff7']
    diff7Ratio = item['value']['diff7Ratio']


    s1 = {'代码': "_"+code,
         '名称': name,
         '1月开盘价': m1open,
         '12月开盘价': m12open,
         '开盘价差': openDiff,
         '12月收盘价': m12close,
         '收盘价差': closeDiff,

         '买点': buy,

         '1月收盘价': close1,
         '1月盈利': diff1,
         '1月盈利百分比': diff1Ratio,

         # '2月收盘价': close2,
         # '2月盈利': diff2,
         # '2月盈利百分比': diff2Ratio,
         #
         # '3月收盘价': close3,
         # '3月盈利': diff3,
         # '3月盈利百分比': diff3Ratio,
         #
         # '4月收盘价': close4,
         # '4月盈利': diff4,
         # '4月盈利百分比': diff4Ratio,
         #
         # '5月收盘价': close5,
         # '5月盈利': diff5,
         # '5月盈利百分比': diff5Ratio,
         #
         # '6月收盘价': close6,
         # '6月盈利': diff6,
         # '6月盈利百分比': diff6Ratio,
         #
         # '7月收盘价': close7,
         # '7月盈利': diff7,
         # '7月盈利百分比': diff7Ratio,
         }

    s2 = {'代码': "_"+code,
         '名称': name,
         '1月开盘价': m1open,
         '12月开盘价': m12open,
         '开盘价差': openDiff,
         '12月收盘价': m12close,
         '收盘价差': closeDiff,

         '买点': buy,

         '1月收盘价': close1,
         '1月盈利': diff1,
         '1月盈利百分比': diff1Ratio,

         '2月收盘价': close2,
         '2月盈利': diff2,
         '2月盈利百分比': diff2Ratio,
         }

    s3 = {'代码': "_"+code,
          '名称': name,
          '1月开盘价': m1open,
          '12月开盘价': m12open,
          '开盘价差': openDiff,
          '12月收盘价': m12close,
          '收盘价差': closeDiff,

          '买点': buy,

          '1月收盘价': close1,
          '1月盈利': diff1,
          '1月盈利百分比': diff1Ratio,

          '3月收盘价': close3,
          '3月盈利': diff3,
          '3月盈利百分比': diff3Ratio,
          }

    s4 = {'代码': "_"+code,
          '名称': name,
          '1月开盘价': m1open,
          '12月开盘价': m12open,
          '开盘价差': openDiff,
          '12月收盘价': m12close,
          '收盘价差': closeDiff,

          '买点': buy,

          '1月收盘价': close1,
          '1月盈利': diff1,
          '1月盈利百分比': diff1Ratio,

          '4月收盘价': close4,
          '4月盈利': diff4,
          '4月盈利百分比': diff4Ratio,
          }

    s5 = {'代码': "_"+code,
          '名称': name,
          '1月开盘价': m1open,
          '12月开盘价': m12open,
          '开盘价差': openDiff,
          '12月收盘价': m12close,
          '收盘价差': closeDiff,

          '买点': buy,

          '1月收盘价': close1,
          '1月盈利': diff1,
          '1月盈利百分比': diff1Ratio,

          '5月收盘价': close5,
          '5月盈利': diff5,
          '5月盈利百分比': diff5Ratio,
          }

    s6 = {'代码': "_"+code,
          '名称': name,
          '1月开盘价': m1open,
          '12月开盘价': m12open,
          '开盘价差': openDiff,
          '12月收盘价': m12close,
          '收盘价差': closeDiff,

          '买点': buy,

          '1月收盘价': close1,
          '1月盈利': diff1,
          '1月盈利百分比': diff1Ratio,

          '6月收盘价': close6,
          '6月盈利': diff6,
          '6月盈利百分比': diff6Ratio,
          }

    s7 = {'代码': "_"+code,
          '名称': name,
          '1月开盘价': m1open,
          '12月开盘价': m12open,
          '开盘价差': openDiff,
          '12月收盘价': m12close,
          '收盘价差': closeDiff,

          '买点': buy,

          '1月收盘价': close1,
          '1月盈利': diff1,
          '1月盈利百分比': diff1Ratio,

          '7月收盘价': close7,
          '7月盈利': diff7,
          '7月盈利百分比': diff7Ratio,
          }

    data_list1.append(s1)
    data_list2.append(s2)
    data_list3.append(s3)
    data_list4.append(s4)
    data_list5.append(s5)
    data_list6.append(s6)
    data_list7.append(s7)

allData = []

allData.append(data_list2)
allData.append(data_list3)
allData.append(data_list4)
allData.append(data_list5)
allData.append(data_list6)
allData.append(data_list7)

# print(data_list2)

book = Workbook()

for index, item in enumerate(allData):

    sheet = book.add_sheet(str(index+2)+'月')
    data = formatData(item, getHeader(index+2))
    insertData(sheet, data)


book.save('longtermOverExcelExport.xls')

#

# header = getHeader(12)
#
# print(header)

# result = pd.DataFrame(data_list, columns=['代码', '名称', '1月开盘价',
#                                           '12月开盘价', '开盘价差', '12月收盘价', '收盘价差','买点',
#                                           '1月收盘价','1月盈利','1月盈利百分比',
#                                           '2月收盘价','2月盈利','2月盈利百分比',
#                                           '3月收盘价','3月盈利','3月盈利百分比',
#                                           '4月收盘价','4月盈利','4月盈利百分比',
#                                           '5月收盘价','5月盈利','5月盈利百分比',
#                                           '6月收盘价','6月盈利','6月盈利百分比',
#                                           '7月收盘价','7月盈利','7月盈利百分比',
#                                           ])
# result[["代码"]] = result[["代码"]].astype('string')
# result.to_csv("~/longterm_stock.csv", encoding="gbk", index=False)

print("............end 1111111111111.........")
