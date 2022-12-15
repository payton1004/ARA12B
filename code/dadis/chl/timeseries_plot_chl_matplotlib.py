import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
from datetime import timedelta
import os
import functools
from matplotlib import dates

cruise='ARA12B'

# DaDiS Fluorometer data
folder_name = 'DaDis'
subfolder_name = 'Fluorometer'
_col = 'Fluorescence' 

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'FM_all_filter_chl_10min_mean.csv'
df = pd.read_csv(_dir+fname, parse_dates=[0])

af = df[['UTC', 'Longitude, mean', 'Latitude, mean', 'Fluorescence, mean', 'Fluorescence, std', 'Fluorescence, count']].dropna()
af.rename(columns={'Longitude, mean':'lon', 'Latitude, mean':'lat', 'Fluorescence, mean':_col}, inplace=True)

# xlabel='Date'
# ylabel='Fluorescence ($^\circ$C)'

# xcol='UTC'
# ycol=_col


import matplotlib
hfmt=matplotlib.dates.DateFormatter('%d-%b')

fig, ax = plt.subplots(1, 1, figsize=(15,4))
# fig.suptitle("$p$CO$_2$, $x$CO$_2$ during ARA12B, 2018", size=15, weight='bold')
# ax.tick_params(direction='in', top=True, right=True)
af.plot(x='UTC', y=_col,  linestyle='-',marker='o', markersize=5, alpha=.5, mfc='None', mec='blue', color='blue', ax=ax, legend=None, clip_on=False, zorder=100)
# ax.axhline(y=0, ls='--', color='red', lw=1)
ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.set_ylim(0, 165)
ax.xaxis.set_major_formatter(hfmt)
_dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname='timeseries_plot_chl_10min_mean.png'
plt.savefig(_dir+fname) 
# plt.show()

fig, ax = plt.subplots(1, 1, figsize=(15,4))
# fig.suptitle("$p$CO$_2$, $x$CO$_2$ during ARA12B, 2018", size=15, weight='bold')
# ax.tick_params(direction='in', top=True, right=True)
af.plot(x='UTC', y=_col,  linestyle='-',marker='o', markersize=5, alpha=.5, mfc='None', mec='blue', color='blue', ax=ax, legend=None, clip_on=False, zorder=100, logy=True)
# ax.axhline(y=0, ls='--', color='red', lw=1)
ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
ax.set_xlabel('Date', weight = 'semibold')
# ax.set_ylim(0, 165)
ax.xaxis.set_major_formatter(hfmt)
_dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname='timeseries_plot_chl_10min_mean_semilogy.png'
plt.savefig(_dir+fname) 
# plt.show()


# cm = plt.cm.get_cmap('RdYlBu')

# fig, ax = plt.subplots(1, 1, figsize=(15,4))
# sc = plt.scatter(af['UTC'], af['Fluorescence'], c=af['Fluorescence'], s=35, cmap=cm)
# ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
# ax.set_xlabel('Date', weight = 'semibold')
# ax.xaxis.set_major_formatter(hfmt)
# plt.colorbar(sc)
# # plt.show()

# pp=10
# np.percentile(af[_col], pp)
for pp in [0.1, 1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99]:
    print(pp, np.percentile(af[_col], pp))
# min    2.386192
# 0.1 2.56345045
# 1 3.0007016666666666
# 5 7.703731666666667
# 10 8.32333
# 20 9.052798333333334
# 30 9.464658684210526
# 40 9.788621666666666
# 50 10.099991666666666
# 60 10.598735
# 70 11.347373333333332
# 80 13.283181666666666
# 90 17.561638333333335
# 95 26.872435833333334
# 99 74.92800687039002
# max  159.297235

# 10 8.3
# 20 9.1 
# 30 9.5
# 40 9.8
# 50 10.1
# 60 10.6
# 70 11.3
# 80 13.3
# 90 17.6


plt.figure(figsize=(10, 10))
plt.hist(af[_col], color = 'green', alpha = 0.4, bins = 100 ,edgecolor='black')
_dir='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/chl/'
fname='histogram_chl.png'    
plt.savefig(_dir+fname)  
# plt.show()

import matplotlib as mpl

#a50026
#d73027
#f46d43
#fdae61
#fee090
#e0f3f8
#abd9e9
#74add1
#4575b4
#313695


# '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#fee090', '#fdae61', '#f46d43', '#d73027' 
cm = (mpl.colors.ListedColormap(['#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#fee090', '#fdae61', '#f46d43', '#d73027' ]).with_extremes(over='#67001f', under='#1a1a1a'))
# cm = (mpl.colors.ListedColormap([[116,173,209],[171,217,233],[224,243,248],[255,255,191],[254,224,144],[253,174,97],[244,109,67]]).with_extremes(over=[215,48,39], under=[69,117,180]))
bounds = [8.3, 9.1, 9.5, 9.8, 10.1, 10.6, 11.3, 13.3, 17.6]
# bounds = [3.0, 7.7, 8.3, 9.0, 9.8, 10.6, 13.3, 26.9]
norm = mpl.colors.BoundaryNorm(bounds, cm.N)

fig, ax = plt.subplots(1, 1, figsize=(15,4))
# sc = plt.scatter(af['UTC'], af[_col], c=af[_col], s=35, cmap=cm, norm=norm, edgecolors='black', alpha=0.5)
sc = plt.scatter(af['UTC'], af[_col], c=af[_col], s=35, cmap=cm, norm=norm, edgecolors=(0,0,0,0.05))
ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(hfmt)
plt.colorbar(sc,  boundaries=[2.0] + bounds + [160], extend='both')
# plt.tight_layout() 
plt.subplots_adjust(left=0.08, right=1.075)
_dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname='timeseries_plot_chl_10min_mean_cb_10_RdYlBu.png'
plt.savefig(_dir+fname) 
plt.show()

# fig, ax = plt.subplots(1, 1, figsize=(15,4))
# # sc = plt.scatter(af['UTC'], af[_col], c=af[_col], s=35, cmap=cm, norm=norm, edgecolors='black', alpha=0.5)
# sc = plt.scatter(af['UTC'], af[_col], c=af[_col], s=35, cmap=cm, norm=norm, edgecolors=(0,0,0,0.05))
# ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
# ax.set_xlabel('Date', weight = 'semibold')
# # Set logarithmic scale on the y variable
# ax.set_yscale("log")
# ax.xaxis.set_major_formatter(hfmt)
# plt.colorbar(sc,  boundaries=[2.0] + bounds + [160], extend='both')
# # plt.tight_layout() 
# plt.subplots_adjust(left=0.08, right=1.075)
# _dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
# fname='timeseries_plot_chl_10min_mean_cb_9_RdYlBu_semilogy.png'
# plt.savefig(_dir+fname) 
# plt.show()

# cm = (mpl.colors.ListedColormap(["royalblue","mediumseagreen","darkorchid", "darkorange","yellow","saddlebrown","violet"]).with_extremes(over='darkgray', under='crimson'))
# # cm = (mpl.colors.ListedColormap(['#91bfdb', '#e0f3f8', '#ffffbf','#fee090','#fc8d59']).with_extremes(over='#d73027', under='#4575b4'))
# # bounds = [3, 8, 9, 10, 11, 13, 18, 27]
# bounds = [3.0, 7.7, 8.3, 9.0, 9.8, 10.6, 13.3, 26.9]
# norm = mpl.colors.BoundaryNorm(bounds, cm.N)

# fig, ax = plt.subplots(1, 1, figsize=(15,4))
# sc = plt.scatter(af['UTC'], af[_col], c=af[_col], s=35, cmap=cm, norm=norm, edgecolors=(0,0,0,0.05))
# ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
# ax.set_xlabel('Date', weight = 'semibold')
# ax.xaxis.set_major_formatter(hfmt)
# plt.colorbar(sc,  boundaries=[2.0] + bounds + [160], extend='both')
# # plt.tight_layout() 
# plt.subplots_adjust(left=0.08, right=1.075)
# _dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
# fname='timeseries_plot_chl_10min_mean_cb_9_set1.png'
# plt.savefig(_dir+fname) 
# # plt.show()

# fig, ax = plt.subplots(1, 1, figsize=(15,4))
# sc = plt.scatter(af['UTC'], af[_col], c=af[_col], s=35, cmap=cm, norm=norm, edgecolors=(0,0,0,0.05))
# ax.set_ylabel('Chlorophyll-a ($\mu$g/L)', weight = 'semibold')
# ax.set_xlabel('Date', weight = 'semibold')
# # Set logarithmic scale on the y variable
# ax.set_yscale("log")
# ax.xaxis.set_major_formatter(hfmt)
# plt.colorbar(sc,  boundaries=[2.0] + bounds + [160], extend='both')
# # plt.tight_layout() 
# plt.subplots_adjust(left=0.08, right=1.075)
# _dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
# fname='timeseries_plot_chl_10min_mean_cb_9_set1_semilogy.png'
# plt.savefig(_dir+fname) 
# # plt.show()