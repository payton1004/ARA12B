from cProfile import label
import datetime
import os
import string
import timeit
from glob import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import dates
from scipy.stats import linregress
import matplotlib

cruise = 'ARA12B'
# 2021-07-20 00:00:00 2021-08-18 23:59:00

# DaDiS Fluorometer data
folder_name = 'DaDis'
subfolder_name = 'Fluorometer'


_col = 'Fluorescence'

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'FM_all_filter_chl.csv'

df = pd.read_csv(_dir+fname, index_col=[0], parse_dates=[0])

# (-180 ~ 180) to (0 ~ 360) 
df['Lon [degree]'] = np.where(df['Longitude']<0, df['Longitude'] + 360, df['Longitude'])
df['Lat [degree]']=df['Latitude']   

# ### check duplicates
# for i in np.arange(len(list(df.index))-1):
#     t1=df.index[i]
#     t2=df.index[i+1]
#     t=t2-t1
#     if (t.components.days==0)&(t.components.hours==0)&(t.components.minutes==0)&(t.components.seconds==0):
#         print(i,t1,t2)

# print(df[df.index=='2021-08-09 15:44:23'])

# # delete rows
# df = df.drop(df[(df['Longitude']==-171.9739)&(df['Latitude']==75.2451)&(df['Latitude']!=-0.5987)].index)

# df.index.is_unique

ef = pd.DataFrame()

ef['Longitude, mean']=df[df['filter_chl']==1.]['Lon [degree]'].resample('10T').mean()
ef['Latitude, mean']=df[df['filter_chl']==1.]['Lat [degree]'].resample('10T').mean()
ef['Fluorescence, mean']=df[df['filter_chl']==1.]['Fluorescence'].resample('10T').mean()

ef['Fluorescence, std']=df[df['filter_chl']==1.]['Fluorescence'].resample('10T').std()
ef['Fluorescence, count']=df[df['filter_chl']==1.]['Fluorescence'].resample('10T').count()

upsampled = df.resample('1s').asfreq()

mf = pd.merge(upsampled, ef, left_index=True, right_index=True, how='outer')

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'FM_all_filter_chl_10min_mean.csv'
mf.to_csv(_dir+fname, index=True, na_rep=np.nan)

# af = mf[['Longitude, mean', 'Latitude, mean', 'Fluorescence SBE45, mean', 'Fluorescence SBE45, std', 'Fluorescence SBE45, count']].dropna()
# af.rename(columns={'Longitude, mean':'lon', 'Latitude, mean':'lat', 'Fluorescence SBE45, mean':_col}, inplace=True)

import matplotlib
hfmt=matplotlib.dates.DateFormatter('%d-%b')
fig, ax = plt.subplots(1, 1, figsize=(15,4), sharex=True)
# fig.suptitle("$p$CO$_2$, $x$CO$_2$ during ARA12B, 2018", size=15, weight='bold')
ax.tick_params(direction='in', top=True, right=True)
# ax.plot(mf.index, mf[_col],  linestyle=' ',marker='o', markersize=3, alpha=.1, mfc="None", mec='gray', label='including outlier')
ax.plot(mf[(mf['filter_chl']==1)].index, mf[(mf['filter_chl']==1)][_col],  linestyle=' ',marker='o', markersize=4, alpha=.1, mfc='None', mec='navy', label='filtering')
ax.plot(mf.index, mf['Fluorescence, mean'],  linestyle=' ',marker='o', markersize=2, alpha=.7, mfc='yellow', mec='None', label='filtering, 10 min. mean')
ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(hfmt)
plt.legend()
_dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'chl_filtering_10min_mean.png'
plt.savefig(_dir+fname) 
# plt.show()