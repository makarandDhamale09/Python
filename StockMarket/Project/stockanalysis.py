# -*- coding: utf-8 -*-
"""StockAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C-cNHyxoYqwDeyQvxBj-r4fEcP0XEIp7
"""

import datetime as dt
from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from jugaad_data.nse import stock_df
import pandas as pd

date_time = dt.datetime.now() - dt.timedelta(days=1)
year = date_time.year
month = date_time.month
day = date_time.day

file_name = bhavcopy_save(date(year, month, day), "sample_data/")
file_name

df = pd.read_csv(file_name)
df

df = df[["SYMBOL", "OPEN", "CLOSE", "TOTTRDQTY", "TOTALTRADES"]]

df['CHANGE'] = ((df['CLOSE'] - df['OPEN']) * 100) / df['OPEN']
df['CHANGE'] = df['CHANGE'].round(2)
df = df.sort_values(["CHANGE", "TOTTRDQTY"], ascending=[0, 0])
df

df = df[df['TOTTRDQTY'] > 10000000]
print(df.head(20))
