import gdown
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

# _col = 'SSS'

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'
fname = 'FM_all.csv'
# df = pd.read_csv(_dir+fname, index_col=[0], parse_dates=[0])
df = pd.read_csv(_dir+fname, index_col=None, parse_dates=[0])

# ### check duplicates
# for i in np.arange(len(list(df.index))-1):
#     t1=df.index[i]
#     t2=df.index[i+1]
#     t=t2-t1
#     if (t.components.days==0)&(t.components.hours==0)&(t.components.minutes==0)&(t.components.seconds==0):
#         print(i,t1,t2)
### check duplicates
for i in np.arange(len(list(df.UTC))-1):
    t1=df.UTC[i]
    t2=df.UTC[i+1]
    t=t2-t1
    if (t.components.days==0)&(t.components.hours==0)&(t.components.minutes==0)&(t.components.seconds==0):
        print(i,t1,t2)        

# print(df[df.UTC=='2021-08-09 15:44:23'])

# delete rows
# nf = df.drop(df[(df['Longitude']==-171.9739)&(df['Latitude']==75.2451)&(df['Fluorescence']!=15.330)].index)
nf = df.drop_duplicates(subset=['UTC'], keep='first')

# print(nf[nf.UTC=='2021-08-09 15:44:23'])

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'
fname = 'FM_all_drop_duplicates.csv'
nf.to_csv(_dir+fname, index=False)