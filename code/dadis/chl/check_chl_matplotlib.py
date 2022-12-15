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
# import matplotlib.dates as md
from scipy.stats import linregress
import matplotlib
from torch import sub


cruise = 'ARA12B'
folder_name='DaDis'
subfolder_name = 'Fluorometer'

_col = 'Fluorescence'

_dir='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'
fname = 'FM_all_drop_duplicates.csv'

tf = pd.read_csv(_dir+fname, index_col=[0], parse_dates=[0])
# tf.index.name='UTC'
# 2021-07-01 06:33:25   - 2021-09-23 05:59:57, 10 second interval
tf.columns = tf.columns.str.lstrip()

hfmt=matplotlib.dates.DateFormatter('%d-%b')

# tf[['Fluorescence']].plot(subplots=False, marker='o',alpha=0.2)
# plt.show()

###
fig, ax = plt.subplots(1, 1, figsize=(15,4), sharex=True)
# fig.suptitle("SSS (psu)", size=15, weight='bold')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(tf.index, tf[_col], linestyle=' ',marker='o', markersize=3, alpha=.1, mfc='None', mec='navy', label='Chlorophyll-a')
# ax.legend()
ax.set_xlabel('Date', weight = 'semibold')
ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
ax.xaxis.set_major_formatter(hfmt)
_dir='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/chl/'
fname='chl_plot.png'
plt.savefig(_dir+fname) 
plt.show()    
###

# pp=10
# np.percentile(tf['SSS'], pp)

# ###
# tf['SSS'].plot(marker='o', ms=3, mfc='blue', color='red', alpha=0.1, figsize=(15,4))
# # plt.xlabel('')
# plt.ylabel('SSS (psu)')
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False) # labels along the bottom edge are off
# _dir='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+sensor+'/sss/'
# fname='check_sss.png'    
# plt.savefig(_dir+fname)    
# # plt.show()
# ###

# plt.figure(figsize=(10, 10))
# plt.hist(tf['SSS'], color = 'green', alpha = 0.4, bins = 100 ,edgecolor='black')
# _dir='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+sensor+'/sss/'
# fname='histogram_sss.png'    
# plt.savefig(_dir+fname)  
# # plt.show()



_dir = '/Users/jung-ok/work1/ARA12B/processed/track_sic/'
fname = 'track_sic_all_n3125.csv'
sf = pd.read_csv(_dir+fname, index_col=[3], parse_dates=[3])
# 2021-07-20 00:00:00  - 2021-08-18 23:59:00, 1 minute interval
sf.columns = sf.columns.str.lstrip()

_start = '2021-07-20 12:00:00'
_end = '2021-08-18 12:00:00'

tf_b = tf[(tf.index>=_start)&(tf.index<=_end)]

# fig, ax=plt.subplots(figsize=(10,5))
fig = plt.subplots(figsize=(15, 4))
ax1=plt.subplot(1,1,1)
ax1.tick_params(direction='in', top=True, right=True)
ax1.plot(tf_b.index, tf_b[_col],  linestyle=' ',marker='o',  markersize=3, color='navy', \
         mew=0, alpha=0.2)
ax1.set_ylabel('Chlorophyll-a ($\mu$g/L)', color='navy')
for tl in ax1.get_yticklabels():
    tl.set_color('navy')   
ax2 = ax1.twinx()
ax2.plot(sf.index,sf['SIC [%]'],linestyle=' ',marker='o',markersize=4,color='gray',mew=0,alpha=0.4)
ax2.set_ylabel('SIC (%)', color='gray')
for tl in ax2.get_yticklabels():
    tl.set_color('gray')     

ax1.set_xlabel('Date')
ax2.xaxis.set_major_formatter(hfmt)
_dir='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/chl/'
fname='chl_sic_nearest_twinx_ara12b.png'
# plt.savefig('/Users/jung-ok/work1/hydroc/plot/sst_sic_nearest_twinx.png') 
plt.savefig(_dir+fname) 
plt.show()




