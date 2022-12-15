# import gdown
import pandas as pd
import matplotlib.pyplot as plt
import glob
import datetime
from datetime import timedelta
import numpy as np
import plotly.express as px 


cruise = 'ARA12B'

# DaDiS Fluorometer data

folder_name = 'DaDis'
subfolder_name = 'Fluorometer'
# fname='FM_all.csv'
_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'
fname = 'FM_all_drop_duplicates.csv'

df = pd.read_csv(_dir+fname, parse_dates=[0])


_col = 'Fluorescence'
_part = df[['UTC',_col]]
# df = df[['UTC',_col]][df['Type'].str.replace(' ', '')==_type].rename(columns={"UTC": "time"})

def plot_days(day1: str, df: pd.DataFrame):
    d2 = datetime.datetime.strptime(day1, '%Y-%m-%d') + timedelta(days=9)
    day2= d2.strftime('%Y-%m-%d')     
    days = df[
        (df["UTC"] >= f"{day1} 00:00:00")
        & (df["UTC"] <= f"{day2} 23:59:59")
    ]
    fig = px.line(days, x="UTC", y=_col, markers=True)
    fig.update_traces(marker_size=5, marker_color='blue', line_color='red', line_width =3, marker_opacity=0.25)
    folder_name='DaDiS'
    fname=day1+'_'+day2+'_chl.html'
    # fname=input('fname = ')
    _file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'+fname
    fig.write_html(_file)
    # fig.show()  

# 시작 0        2021-07-01 06:33:25
# 끝 724439   2021-09-23 05:59:57


d1_str = '2021-07-04'           
plot_days(d1_str, _part[['UTC',_col]])

d1_str = '2021-07-14'          
plot_days(d1_str, _part[['UTC',_col]])

d1_str = '2021-07-24'             
plot_days(d1_str, _part[['UTC',_col]])

d1_str = '2021-08-03'              
plot_days(d1_str, _part[['UTC',_col]])

d1_str = '2021-08-13'         
plot_days(d1_str, _part[['UTC',_col]])




