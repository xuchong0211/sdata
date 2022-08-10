import baostock as bs
import pandas as pd
from datetime import date, timedelta, datetime
import numpy as np
from dateutil.relativedelta import relativedelta


a = [3, 2, 1]


print(a)
b = "2022-08-09"

c = (datetime.strptime(b, "%Y-%m-%d") + timedelta(days=8)).strftime("%Y%m%d")

print(c)

# today = date.today()
#
# todayStr = today.strftime("%Y-%m-%d")
#
# startDateStr = (date.today() + timedelta(weeks=-500)).strftime("%Y-%m-%d")


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
