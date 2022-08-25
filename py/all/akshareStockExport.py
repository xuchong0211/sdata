import requests
import pandas as pd
import codecs
import json
from datetime import date, timedelta
import numpy as np



today = date.today().strftime("%Y%m%d")
# today = "20220729"

urls =[
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/dayou",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/doublelong",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/fankeweizhuplus",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/feilong",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniu",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/gesandaniuplus",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/jianlongplus",
    "http://admin:password@127.0.0.1:5984/daily_"+today+"_fast/_design/list/_view/shenlong3",
      ]

note = open(today + ".txt", mode='w')
note.write(today + "    \n")

for url in urls:
    print("=========================== start ===================================")
    print(url)
    urlstr= url.split('/')
    mode = urlstr[len(urlstr)-1]
    print(mode)

    res = requests.get(url)

    data = res.json()
    data = data["rows"]

    print(data)

    note.write(mode + "    \n")
    note.write("\n")
    note.write("\n")
    note.write(str(data) + "    \n")
    note.write("\n")
    note.write("\n")

note.close()


# urls = url.split('/')
# mode = urls[len(urls)-1]


print("............end.........")
