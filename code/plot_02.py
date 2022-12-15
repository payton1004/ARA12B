import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
import datetime
import re
import os
from glob import glob
import numpy as np
import string
from matplotlib import dates
import timeit

cruise = 'ARA12B'
d1 = '2021-07-20 12:00'
d2 = '2021-08-18 12:00'



# Optode O2 [uM]
folder_name='Optode'
_col = 'O2 [uM]'
_ylabel = 'O$_2$ [$\mu$M]'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'o2_flag.csv'

df=pd.read_csv(_file, index_col=[0], parse_dates=True)


dg = df[(df.index >=d1) & (df.index <=d2)&(df['flag']==1)].resample('10min').mean()

# dg = df[df['flag']==1].resample('10min').mean()

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'o2_10min.csv'
dg.dropna().to_csv(_file, na_rep=np.nan, index=True, float_format='%g')

dg=pd.read_csv(_file, parse_dates=True, index_col=[0])



matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

# hfmt=matplotlib.dates.DateFormatter('%d-%b')
date_fmt = '%d-%b'
date_formatter = dates.DateFormatter(date_fmt)


fig, ax = plt.subplots(1, 1, figsize=(16,7))
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# fig.suptitle("Dissolved Oxygen measured by Optode during ARA09B, 2018", size=15, weight='bold')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(dg.index, dg[_col],  linestyle='-',marker='o', markersize=7, alpha=.5, color='blue',clip_on=False, zorder=100, markerfacecolor='red', markeredgecolor='black')
ax.set_ylabel(_ylabel, weight='semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(date_formatter)
# ax.xaxis.set_major_formatter(hfmt)

_file ='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/anom03/'+'optode_o2_10min.png'
plt.savefig(_file)
plt.show()



# HydroC pCO2_corr

folder_name='HydroC_pCO2'
_col = 'pCO2_corr'
_ylabel = '$p$CO$_2$ [$\mu$atm]'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'hydroc_pco2_flag.csv'

df=pd.read_csv(_file, index_col=[0], parse_dates=True)


dg = df[(df.index >=d1) & (df.index <=d2)&(df['flag']==1)].resample('10min').mean()

# dg = df[df['flag']==1].resample('10min').mean()

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'pco2_10min.csv'
dg.dropna().to_csv(_file, na_rep=np.nan, index=True, float_format='%g')

dg=pd.read_csv(_file, parse_dates=True, index_col=[0])


matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

hfmt=matplotlib.dates.DateFormatter('%d-%b')
fig, ax = plt.subplots(1, 1, figsize=(16,7))
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# fig.suptitle("Dissolved Oxygen measured by Optode during ARA09B, 2018", size=15, weight='bold')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(dg.index, dg[_col],  linestyle='-',marker='o', markersize=7, alpha=.5, color='blue',clip_on=False, zorder=100, markerfacecolor='red', markeredgecolor='black')
ax.set_ylabel(_ylabel, weight='semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(date_formatter)
_file ='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/anom03/'+'hydroc_pco2_10min.png'
plt.savefig(_file)
plt.show()

# GO 141  ATM CO2 um/m
folder_name='GO_pCO2'

_col = 'CO2 um/m'
_ylabel = 'xCO$_2$ [ppm]'

_type ='ATM'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom01/'+'atm_flag.csv'
df=pd.read_csv(_file, index_col=[0], parse_dates=True)


# dg = df[(df.index >=d1) & (df.index <=d2)&(df['flag']==1)].resample('10min').mean()
dg = df[(df.index >=d1) & (df.index <=d2)&(df['flag']==1)].resample('1min').mean()


_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom01'+'/'+'go141_pco2_atm_1min.csv'
dg.dropna().to_csv(_file, na_rep=np.nan, index=True, float_format='%g')

dg=pd.read_csv(_file, index_col=[0], parse_dates=True)

matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

hfmt=matplotlib.dates.DateFormatter('%d-%b')
fig, ax = plt.subplots(1, 1, figsize=(16,7))
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# fig.suptitle("Dissolved Oxygen measured by Optode during ARA09B, 2018", size=15, weight='bold')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(dg.index, dg[_col],  linestyle='-',marker='o', markersize=7, alpha=.5, color='blue',clip_on=False, zorder=100, markerfacecolor='red', markeredgecolor='black')
ax.set_ylabel(_ylabel, weight='semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(date_formatter)
_file ='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+_type+'/'+'anom01'+'/'+'go141_pco2_atm.png'
plt.savefig(_file)
plt.show()

# GO 141  EQU CO2 um/m
folder_name='GO_pCO2'
_type ='EQU'
_col = 'CO2 um/m'
_ylabel = 'xCO$_2$ [ppm]'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom03/'+'equ_flag.csv'

df=pd.read_csv(_file, index_col=[0], parse_dates=True)
###
dg = df[(df.index >=d1) & (df.index <=d2)&(df['flag']==1)].resample('10min').mean()
# dg = df[df['flag']==1].resample('10min').mean()

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom03'+'/'+'go141_pco2_equ_10min.csv'
dg.dropna().to_csv(_file, na_rep=np.nan, index=True, float_format='%g')
dg=pd.read_csv(_file, parse_dates=True, index_col=[0])


matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

hfmt=matplotlib.dates.DateFormatter('%d-%b')
fig, ax = plt.subplots(1, 1, figsize=(16,7))
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# fig.suptitle("Dissolved Oxygen measured by Optode during ARA09B, 2018", size=15, weight='bold')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(dg.index, dg[_col],  linestyle='-',marker='o', markersize=7, alpha=.5, color='blue',clip_on=False, zorder=100, markerfacecolor='red', markeredgecolor='black')
ax.set_ylabel(_ylabel, weight='semibold')
ax.set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(date_formatter)
_file ='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+_type+'/'+'anom03'+'/'+'go141_pco2_equ_10min.png'
plt.savefig(_file)
plt.show()

# ATM, EQU
# GO 141  CO2 um/m
folder_name='GO_pCO2'
_col = 'CO2 um/m'
_ylabel = 'xCO$_2$ [ppm]'


_type ='EQU'
# _file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom03/'+'equ_flag.csv'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom03'+'/'+'go141_pco2_equ_10min.csv'
equ=pd.read_csv(_file, index_col=[0], parse_dates=True)
# equ = df_equ[df_equ['flag']==1]

_type ='ATM'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom01'+'/'+'go141_pco2_atm_1min.csv'
atm=pd.read_csv(_file, index_col=[0], parse_dates=True)
# atm = df_atm[df_atm['flag']==1]

# _file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom01'+'/'+'go141_pco2_equ_10min.csv'
# dg.to_csv(_file, na_rep=np.nan, index=True, float_format='%g')


matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

hfmt=matplotlib.dates.DateFormatter('%d-%b')
fig, axes = plt.subplots(2, 1, figsize=(16,7),sharex=True)
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# fig.suptitle("Dissolved Oxygen measured by Optode during ARA09B, 2018", size=15, weight='bold')
axes[0].tick_params(direction='in', top=True, right=True)
axes[1].tick_params(direction='in', top=True, right=True)
# plt.legend()
axes[0].plot(atm.index, atm[_col],  linestyle='-',marker='o', markersize=7, alpha=.5, color='blue',clip_on=False, zorder=100, label='air', markerfacecolor='blue', markeredgecolor='darkblue')
axes[0].legend()
axes[1].plot(equ.index, equ[_col],  linestyle='-',marker='o', markersize=7, alpha=.5, color='green',clip_on=False, zorder=100, label='seawater', markerfacecolor='green', markeredgecolor='darkgreen')
axes[1].legend()
axes[0].set_ylabel(_ylabel, weight='semibold')
# axes[0].set_xlabel('', weight = 'semibold')
axes[1].set_xlabel('Date', weight = 'semibold')
ax.xaxis.set_major_formatter(date_formatter)

_file ='/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+'/'+'go141_pco2_equ_atm.png'
plt.savefig(_file)
plt.show()
