# import gdown
import pandas as pd
import matplotlib.pyplot as plt
import glob
import datetime
from datetime import timedelta
import numpy as np
import plotly.express as px 
import functools

print('run anom03-3.py')

cruise = 'ARA12B'

# DaDiS Fluorometer data
folder_name='DaDiS'
subfolder_name = 'Fluorometer'

# start 0        2021-07-01 06:33:25
# end   724439   2021-09-23 05:59:57

_col = 'Fluorescence'

mf = pd.concat(map(functools.partial(pd.read_csv, delimiter=','), 
            sorted(glob.glob('/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom03/'+'2021*.csv')))) 

_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom03/'+'chl_flag.csv'
mf.sort_values(by='UTC').to_csv(_file, index=False, na_rep=np.nan, float_format='%g')            


def plot_days(day1: str, df: pd.DataFrame):
    d2 = datetime.datetime.strptime(day1, '%Y-%m-%d') + timedelta(days=9)
    day2= d2.strftime('%Y-%m-%d')     
    days = df[
        (df["UTC"] >= f"{day1} 00:00:00")
        & (df["UTC"] <= f"{day2} 23:59:59")
    ]
    fig = px.line(days, x="UTC", y=_col, markers=True)
    fig.update_traces(marker_size=5, marker_color='blue', line_color='red', line_width =3, marker_opacity=0.25)
    # folder_name='DaDiS'
    fname=day1+'_'+day2+'.html'
    # fname=input('fname = ')
    _file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom03/'+fname
    fig.write_html(_file)
    # fig.show() 


# normal
nf = mf[mf['flag']==1].sort_values(by='UTC').drop(columns='flag')
# anomaly
af = mf[mf['flag']==0].sort_values(by='UTC').drop(columns='flag')



d1_str = '2021-07-04'           
plot_days(d1_str, nf)

# d1_str = '2021-07-04'           
# plot_days(d1_str, af)

d1_str = '2021-07-14'          
plot_days(d1_str, nf)

d1_str = '2021-07-24'             
plot_days(d1_str, nf)

d1_str = '2021-08-03'              
plot_days(d1_str, nf)

d1_str = '2021-08-13'         
plot_days(d1_str, nf)




