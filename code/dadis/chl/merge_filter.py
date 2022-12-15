# import gdown
import pandas as pd
import matplotlib.pyplot as plt
import glob
import datetime
from datetime import timedelta
import numpy as np
import plotly.express as px 

cruise = 'ARA12B'
# 2021-07-20 00:00:00 2021-08-18 23:59:00

# DaDiS Fluorometer data
folder_name = 'DaDis'
subfolder_name = 'Fluorometer'

# start         2021-07-04 01:38:43
# end           2021-08-22 23:59:56

_col = 'Fluorescence'

# fname='FM_all.csv'
fname = 'FM_all_drop_duplicates.csv'
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+fname

df = pd.read_csv(_file, index_col=[0], parse_dates=[0])
df_b = df[(df.index>='2021-07-20 12:00:00')&(df.index<='2021-08-18 12:00:00')]
# df_b = df[(df.index>='2021-07-20 00:00:00')&(df.index<='2021-08-18 23:59:00')]


# df_b[_col].plot(marker='o', ls='', alpha=0.1, figsize=(15, 8))
# plt.show()



# SBE45, filtered
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/anom05/'+'chl_flag.csv'
ff_chl = pd.read_csv(_file, index_col=[0], parse_dates=[0])
ff_chl.rename(columns={'flag':'filter_chl', 'Fluorescence':'Fluorescence, filtered'}, inplace=True)
ff_chl_b = ff_chl[(ff_chl.index>='2021-07-20 12:00:00')&(ff_chl.index<='2021-08-18 12:00:00')]



mf = pd.merge(df_b, ff_chl_b['filter_chl'], left_index=True, right_index=True, how='outer')

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'FM_all_filter_chl.csv'
mf.to_csv(_dir+fname, index=True, na_rep=np.nan)


import matplotlib
hfmt=matplotlib.dates.DateFormatter('%d-%b')
fig, ax = plt.subplots(1, 1, figsize=(15,4), sharex=True)
# fig.suptitle("$p$CO$_2$, $x$CO$_2$ during ARA12B, 2018", size=15, weight='bold')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(mf.index, mf[_col],  linestyle=' ',marker='o', markersize=3, alpha=.1, mfc="None", mec='gray', label='including outlier')
ax.plot(mf[(mf['filter_chl']==1)].index, mf[(mf['filter_chl']==1)][_col],  linestyle=' ',marker='o', markersize=3, alpha=.2, mfc='navy', mec='navy', label='filtering')
ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(hfmt)
plt.legend()
_dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'chl_including_outlier_filtering.png'
plt.savefig(_dir+fname) 
# plt.show()