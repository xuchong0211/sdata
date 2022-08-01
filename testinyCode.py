import baostock as bs
import pandas as pd
from datetime import date, timedelta
import numpy as np

a = [3, 2, 1]


print(a)

today = date.today()

todayStr = today.strftime("%Y-%m-%d")

startDateStr = (date.today() + timedelta(weeks=-500)).strftime("%Y-%m-%d")


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