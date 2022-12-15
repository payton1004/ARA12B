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

date_fmt = '%d-%b-%Y %H:%M'
date_formatter = dates.DateFormatter(date_fmt)

# def plot_DO2Ar(df):
#     fig, ax = plt.subplots(1, 1, figsize=(12, 8) ,sharex=True)
#     df.plot(x='UTC', y='DO2/Ar (%)', 
#     ax=ax, ls=' ',marker='o',  ms=7, mfc="blue", mew=0.25, alpha=.5, mec='black',clip_on=False, zorder=100, legend=False)
#     ax.set_ylabel('$\Delta$O$_2$/Ar (%)', weight = 'semibold')
#     ax.set_xlabel('Date', weight = 'semibold')
#     _dir='/Users/jung-ok/work1/ARA12B/plot/EIMS/'
#     fname='DO2Ar_10min.png'
#     plt.savefig(_dir+fname)
#     plt.show()


# def plot_air_saturation(df, _dir, fname, iname, xcol, ycol, xlabel, ylabel):
#     fig, ax = plt.subplots(1, 1, figsize=(12, 8))
#     df.plot(x=xcol, y=ycol, 
#     ax=ax, ls=' ',marker='o',  ms=7, mfc="blue", mew=0.25, alpha=.5, mec='black',clip_on=False, zorder=100, label=iname)
#     ax.set_ylabel(ylabel, weight = 'semibold')
#     ax.set_xlabel(xlabel, weight = 'semibold')
#     ax.xaxis.set_major_formatter(date_formatter)
#     plt.savefig(_dir+fname)
#     plt.show()

def plot_01(df, _dir, fname, iname, xcol, ycol, xlabel, ylabel):
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    df.plot(x=xcol, y=ycol, 
    ax=ax, ls=' ',marker='o',  ms=7, mfc="blue", mew=0.25, alpha=.5, mec='black',clip_on=False, zorder=100, label=iname)
    ax.set_ylabel(ylabel, weight = 'semibold')
    ax.set_xlabel(xlabel, weight = 'semibold')
    ax.xaxis.set_major_formatter(date_formatter)
    plt.savefig(_dir+fname)
    plt.show()   

def plot_02(df1, df2, _dir, fname, xcol1, ycol1, xcol2, ycol2, xlabel, label1, label2):
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    df1.plot(x=xcol1, y=ycol1, 
    ax=ax, ls='',marker='o',  ms=2, mfc="None", mew=0.5, alpha=.75, mec='red',clip_on=False, zorder=100, label=label1)
    df2.plot(x=xcol2, y=ycol2, 
    ax=ax, ls='',marker='o',  ms=2, mfc="None", mew=0.5, alpha=.75, mec='blue',clip_on=False, zorder=100, label=label2)
    # ax.set_ylabel(ylabel, weight = 'semibold')
    ax.set_xlabel(xlabel, weight = 'semibold')
    ax.xaxis.set_major_formatter(date_formatter)
    plt.savefig(_dir+fname)
    plt.show()       

### EIMS
_dir='/Users/jung-ok/work1/ARA12B/processed/EIMS/'
fname='DO2Ar_calibrated_10min.csv'
df = pd.read_csv(_dir+fname, index_col=None, parse_dates=[0])

# plot_DO2Ar(df[df['flag']==1])

df['Air Saturation [%]'] = df['m32m40']/df['O2/Ar_interp'] * 100


### Optode
_dir='/Users/jung-ok/work1/ARA12B/processed/Optode/'
fname='Optode_all_10min.csv'
dg = pd.read_csv(_dir+fname, index_col=None, parse_dates=[0])

dg['DO2 [%]'] = dg['Air Saturation [%]'] - 100


# ### Air Saturation
# xcol='UTC'
# ycol='Air Saturation [%]'
# xlabel='Date'
# ylabel='Air Saturation [%]'

# iname='EIMS'
# _dir='/Users/jung-ok/work1/ARA12B/plot/EIMS/'
# fname='EIMS_Air_Saturation_10min.png'
# plot_01(df[df['flag']==1], _dir, fname, iname, xcol, ycol, xlabel, ylabel)

# iname='Optode'
# _dir='/Users/jung-ok/work1/ARA12B/plot/Optode/'
# fname='Optode_Air_Saturation_10min.png'
# plot_01(dg.dropna(), _dir, fname, iname, xcol, ycol, xlabel, ylabel)

# ### DO2
# xcol='UTC'
# xlabel='Date'

# ycol='DO2/Ar (%)'
# ylabel='$\Delta$O$_2$/Ar [%]'

# iname='EIMS'
# _dir='/Users/jung-ok/work1/ARA12B/plot/EIMS/'
# fname='EIMS_DO2Ar_10min.png'
# plot_01(df[df['flag']==1], _dir, fname, iname, xcol, ycol, xlabel, ylabel)

# ycol='DO2 [%]'
# ylabel='$\Delta$O$_2$/Ar [%]'

# iname='Optode'
# _dir='/Users/jung-ok/work1/ARA12B/plot/Optode/'
# fname='Optode_DO2_10min.png'
# plot_01(dg.dropna(), _dir, fname, iname, xcol, ycol, xlabel, ylabel)

### DO2, EIMS & Optode
xcol1='UTC'
ycol1='DO2/Ar (%)'
xcol2='UTC'
ycol2='DO2 [%]'
xlabel='Date'
label1='EIMS $\Delta$O$_2$/Ar [%]'
label2='Optode $\Delta$O$_2$ [%]'

_dir='/Users/jung-ok/work1/ARA12B/plot/'
fname='EIMS_DO2Ar_Optode_DO2_10min.png'
plot_02(df[df['flag']==1], dg.dropna(), _dir, fname, xcol1, ycol1, xcol2, ycol2, xlabel, label1, label2)



