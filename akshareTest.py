import akshare as ak
import couchdb
import pandas as pd

import datetime
from datetime import timedelta


now = datetime.datetime.now()

#今天
today = now

#昨天
yesterday = now - timedelta(1)


