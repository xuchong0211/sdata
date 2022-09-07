import baostock as bs
import pandas as pd
from datetime import date, timedelta, datetime
import numpy as np
from dateutil.relativedelta import relativedelta
from statistics import mean



def getName(name) :

    if name == "dayou":
      return "大有"

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

print(getName("gesandaniuplus"))


def findHighs(arr):

    arr = np.array(arr)



    indexList =  arr.argsort()[-3:][::-1]


    maximumIndex1 = np.where(arr == arr[indexList[0]])[0]
    maximumIndex2 = np.where(arr == arr[indexList[1]])[0]
    maximumIndex3 = np.where(arr == arr[indexList[2]])[0]
    print ("maximumIndex1", maximumIndex1);
    # print ("maximumIndex2", maximumIndex2);
    # print ("maximumIndex3", maximumIndex3);

    # maximum1 = arr[0]
    # maximum2 = max(arr, key=lambda x: min(arr)-1 if (x == maximum1) else x)
    # maximum3 = max(arr, key=lambda x: min(arr)-2 if (x == maximum2) else x)

    maximumIndex = []
    maximumIndex.append(maximumIndex1[0])
    print ("1111111111111111122222222", maximumIndex)
    if maximumIndex1[0] != maximumIndex2[0]:
        maximumIndex.append(maximumIndex2[0])

    if maximumIndex2[0] != maximumIndex3[0]:
        maximumIndex.append(maximumIndex3[0])

    # print('111111111111111111111111', maximum1)
    # print('2222222222222222222222222222222', maximum2)
    # print('3333333333333333333333333', maximum3)

    # result1 = np.where(arr == maximum1)
    # result2 = np.where(arr == maximum2)
    # result3 = np.where(arr == maximum3)

    print('maximum Index', maximumIndex)
    return maximumIndex


arr = np.array([11, 12, 13, 14, 11, 11, 17, 11, 11, 12, 14, 11, 16, 17])

aaaa = mean(arr)

print("kkkkkkkkkkkkkkkk", aaaa);

resultHighs = findHighs(arr)

print("900000000000000000", resultHighs);

result =  arr.argsort()[-3:][::-1]

print("=======================", result)
print("======================= 111", arr[result[0]])
print("======================= 222", arr[result[1]])
print("======================= 3333", arr[result[2]])


# print('Contents of Numpy array : ', arr, sep='\n')
# print("*** Get Maximum element from a 1D numpy array***")
# # Get the maximum element from a Numpy array
# maxElement = np.amax(arr)
# print('Max element from Numpy Array : ', maxElement)
# print('00000000000000000000000000000000', min(arr))
#
# maximum1 = max(arr)
# maximum2 = max(arr, key=lambda x: min(arr)-1 if (x == maximum1) else x)
# maximum3 = max(arr, key=lambda x: min(arr)-3 if (x == maximum2) else x)
#
#
# print('111111111111111111111111', maximum1)
# print('2222222222222222222222222222222', maximum2)
# print('33333333333333333333333333', maximum3)
#
# result1 = np.where(arr == maximum1)
# result2 = np.where(arr == maximum2)
# result3 = np.where(arr == maximum3)
#
# print('Returned tuple of arrays', result1, result2, result2)

s = [{
      "name": "西部创业",
      "code": "000557",
      "date": "2022-08-24",
      "open": 4.98,
      "close": 5.17,
      "high": 5.17,
      "low": 4.82,
      "volume": 731271,
      "turn": 372702515.88,
      "zhenfu": 7.45,
      "range": 10,
      "amount": 0.47,
      "turnover": 5.02
    },
    {
      "name": "西部创业",
      "code": "000557",
      "date": "2022-08-23",
      "open": 4.52,
      "close": 4.7,
      "high": 4.83,
      "low": 4.48,
      "volume": 249544,
      "turn": 116569802.87,
      "zhenfu": 7.76,
      "range": 4.21,
      "amount": 0.19,
      "turnover": 1.71
    },
    {
      "name": "西部创业",
      "code": "000557",
      "date": "2022-08-22",
      "open": 4.46,
      "close": 4.51,
      "high": 4.52,
      "low": 4.44,
      "volume": 80705,
      "turn": 36186512.66,
      "zhenfu": 1.79,
      "range": 0.67,
      "amount": 0.03,
      "turnover": 0.55
    },
    {
      "name": "西部创业",
      "code": "000557",
      "date": "2022-08-19",
      "open": 4.44,
      "close": 4.48,
      "high": 4.55,
      "low": 4.43,
      "volume": 125773,
      "turn": 56515907.7,
      "zhenfu": 2.7,
      "range": 0.9,
      "amount": 0.04,
      "turnover": 0.86
    }]

# a = [3, 2, 1]
a = np.array(s[0:len(s)-1])

b = np.array(s[1:])

ztlist = ""

for i in range(len(a)) :
  zt = a[i]["close"] == round(b[i]["close"] * 1.1, 2)
  if zt :
    ztlist = ztlist + "1"
  else :
    ztlist = ztlist + "0"

print(a)
print(b)
print("11111111111111111111111111111111")
print(ztlist)

print("=======================================")
print(a)
b = "2022-08-09"

c = (datetime.strptime(b, "%Y-%m-%d") + timedelta(days=8)).strftime("%Y%m%d")

print(c)

# today = date.today()
#
# todayStr = today.strftime("%Y-%m-%d")
#
# startDateStr = (date.today() + timedelta(weeks=-500)).strftime("%Y-%m-%d")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.FAIL}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

a = 1
b = 2

# print("fjdsfjs jdfslf  %a is %b" % {'a': a, 'b': b})
# print("fjdsfjs jdfslf  ", a , sep=", ")

today = date.today().strftime("%Y%m%d")
startDate = (date.today() + relativedelta(months=-8)).strftime("%Y%m%d")

print( today)
print( startDate)


url="http://127.0.0.1:5984/g8_20220729/_design/g8/_view/mai2_3"

urls = url.split('/')

print("=====================")
print(urls[len(urls)-1])
sum = np.array([1,2,3])
print(np.sum(a, axis = 0))

print(todayStr)
print(startDateStr)

count = 1
print("231223" + str(count))
