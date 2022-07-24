import baostock as bs
import pandas as pd
from datetime import date, timedelta
import numpy as np

a = [3, 2, 1]


print(a)

today = date.today()

todayStr = today.strftime("%Y-%m-%d")

startDateStr = (date.today() + timedelta(weeks=-500)).strftime("%Y-%m-%d")


print("=====================")
sum = np.array([1,2,3])
print(np.sum(a, axis = 0))

print(todayStr)
print(startDateStr)

count = 1
print("231223" + str(count))