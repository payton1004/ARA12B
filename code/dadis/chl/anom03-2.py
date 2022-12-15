# import gdown
import pandas as pd
import matplotlib.pyplot as plt
import glob
import datetime
from datetime import timedelta
from matplotlib import dates
import numpy as np
import plotly.express as px 
import functools

print('run anom03-2.py')

cruise = 'ARA12B'


# DaDiS Fluorometer data

# 시작 0        2021-07-01 06:33:25
# 끝 724439   2021-09-23 05:59:57
folder_name = 'DaDis'
subfolder_name = 'Fluorometer'

fname='chl_flag.csv'
# fname=input('fname = ')
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom02/'+fname


df = pd.read_csv(_file, parse_dates=[0])
# df.info()

_col = 'Fluorescence'
_part = df[['UTC',_col]][df['flag']==1]

# date_fmt = '%d-%b-%Y %H:%M'
# date_formatter = dates.DateFormatter(date_fmt)    

# fig, ax=plt.subplots(figsize=(20,10))
# ax.plot(_part['UTC'], _part[_col], marker='o', alpha=0.5, c='blue', mfc='black')
# ax.xaxis.set_major_formatter(date_formatter)
# plt.show()




def save_anomal(day1: str, df: pd.DataFrame, wp: float):
    d2 = datetime.datetime.strptime(day1, '%Y-%m-%d') + timedelta(days=9)
    day2= d2.strftime('%Y-%m-%d')
    print(day1, day2)     
    days = df[
        (df["UTC"] >= f"{day1} 00:00:00")
        & (df["UTC"] <= f"{day2} 23:59:59")
    ]
    data = days.set_index('UTC')
    column = data[_col]

    N = len(column)
    time = np.arange(0,N)
    (len(data[50000:75000]),len(time))

    #parameters
    window_percentage = wp
    k = int(len(column) * (window_percentage/100))
    N = len(column)
    (k,N)

    column = column.to_numpy()

    get_bands = lambda data : (np.mean(data) + 3*np.std(data),np.mean(data) - 3*np.std(data))
    #get_bands = lambda data : (np.mean(data) + np.nanquantile(data,0.99),np.mean(data) - np.nanquantile(data,0.99))

    bands = [get_bands(column[range(0 if i - k < 0 else i-k ,i + k if i + k < N else N)]) for i in range(0,N)]
    upper, lower = zip(*bands)

    # compute local outliers 
    anomalies = (column > upper) | (column < lower)

    new_df = pd.DataFrame(np.array([column, ~anomalies]).T, columns=[_col, 'flag'], index=data.index)

    folder_name='DaDiS'
    # folder_name=input('folder_name = ')
    # fname=day+'.csv'
    fname=day1+'_'+day2+'.csv'
    # fname=input('fname = ')
    _file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom03/'+fname
    new_df.to_csv(_file, na_rep=np.nan, index=True)
    
tdays = pd.date_range(start='07/04/2021', end='08/13/2021', freq='10D')
# for i in np.arange(0,5):
# print(i)
# 0 - 4 (5)
# i : [0,1] 0 ; wp = 0.1
# i : [2,3,4] ; wp = 2.5
i = int(input('i = '))
# window percentage
wp = float(input('wp = '))
day = tdays[i].strftime('%Y-%m-%d')
save_anomal(day, _part[['UTC',_col]], wp)






