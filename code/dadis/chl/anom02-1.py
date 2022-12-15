import gdown
import pandas as pd
import matplotlib.pyplot as plt
import glob
import datetime
from matplotlib import dates
from datetime import timedelta
import numpy as np
import plotly.express as px 

print('run anom02-1.py')

cruise = 'ARA12B'

# DaDiS Fluorometer data

folder_name = 'DaDis'
subfolder_name = 'Fluorometer'

# 시작 0        2021-07-01 06:33:25
# 끝 724439   2021-09-23 05:59:57

_col = 'Fluorescence'

fname='chl_flag.csv'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom01/'+fname

df = pd.read_csv(_file, parse_dates=[0])
# # df.info()

_col = 'Fluorescence'
_part = df[['UTC',_col]][df['flag']==1]



def plot_anomal(day1: str, df: pd.DataFrame, wp: float):
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
    # (len(data),len(time))

    #parameters
    window_percentage = wp
    k = int(len(column) * (window_percentage/100))
    N = len(column)
    # (k,N)

    column = column.to_numpy()

    get_bands = lambda data : (np.mean(data) + 3*np.std(data),np.mean(data) - 3*np.std(data))
    #get_bands = lambda data : (np.mean(data) + np.nanquantile(data,0.99),np.mean(data) - np.nanquantile(data,0.99))

    bands = [get_bands(column[range(0 if i - k < 0 else i-k ,i + k if i + k < N else N)]) for i in range(0,N)]
    upper, lower = zip(*bands)

    # compute local outliers 
    anomalies = (column > upper) | (column < lower)
    
    # plotting...
    plt.figure(figsize=(20,5))
    plt.plot(time,column,'k',label='Data')
    plt.plot(time,upper,'r-',label='Bands',alpha=0.3)
    plt.plot(time,lower,'r-',alpha=0.3)
    plt.plot(time[anomalies],column[anomalies],'ro',label='Anomalies')
    plt.fill_between(time, upper, lower,facecolor='red',alpha=0.1)
    plt.legend()
    # folder_name='DaDiS'
    # folder_name=input('folder_name = ')
    fname=day1+'_'+day2+'.png'
    # fname=input('fname = ')
    _file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom02/'+fname
    plt.savefig(_file)
    # plt.show()


   

tdays = pd.date_range(start='07/04/2021', end='08/13/2021', freq='10D')
for i in np.arange(0,5):
    print(i)
    # 0 - 4 (5)
    # i = 0
    # i = int(input('i = '))
    # window percentage
    # i : [0, 1] , wp = 10
    # i : [2, 3, 4] , wp = 2.5
    wp = 2.5
    # wp = float(input('wp = '))
    day = tdays[i].strftime('%Y-%m-%d')
    plot_anomal(day, _part, wp)







