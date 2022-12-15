## Reformat GPS ##
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import string
from matplotlib import dates
# import matplotlib.dates as md
from scipy.stats import linregress
import os

# import datetime
from datetime import datetime
import timeit

# import pandas_profiling

cruise = 'ARA12B'
# d1 = '2021-07-20 00:00:00'
# d2 = '2021-08-18 23:59:59'
d1 = '2021-07-20 12:00:00'
d2 = '2021-08-18 12:00:00'


# GPS
folder_name = 'DaDiS'
df=pd.read_csv('/Users/jung-ok/work1/ARA12B/processed/DaDiS/GPS_1min_lon_0_360.csv', index_col=None, parse_dates=[0]) 

df.rename(columns={'UTC Time':'UTC'}, inplace=True)
# ['UTC', 'Latitude', 'Longitude']
gps = df[['UTC', 'Longitude', 'Latitude']][(df.UTC >=d1) & (df.UTC <=d2)]

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+'utc_lon_lat_1min.csv'
gps.dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')


# Optode
folder_name='Optode'
_col = 'O2 [uM]'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'o2_10min.csv'
dg=pd.read_csv(_file, index_col=None, parse_dates=[0]) 

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'gps_optode_o2_10min.csv'
gps.merge(dg[['UTC', _col]], how='inner', on='UTC').dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')

gf=pd.read_csv(_file, index_col=None, parse_dates=[0]) 

# HydroC pCO2_corr
folder_name='HydroC_pCO2'
_col = 'pCO2_corr'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'pco2_10min.csv'
dg=pd.read_csv(_file, index_col=None, parse_dates=[0]) 

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'gps_hydroc_pco2_10min.csv'
gps.merge(dg[['UTC', _col]], how='inner', on='UTC').dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')

gf=pd.read_csv(_file, index_col=None, parse_dates=[0]) 
# gf

# GO 141  ATM CO2 um/m
folder_name='GO_pCO2'
_col = 'CO2 um/m'
_type ='ATM'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom01'+'/'+'go141_pco2_atm_1min.csv'
dg=pd.read_csv(_file, index_col=None, parse_dates=[0]) 

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom01'+'/'+'gps_go141_pco2_atm_1min.csv'
gps.merge(dg[['UTC', _col]], how='inner', on='UTC').dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')

gf=pd.read_csv(_file, index_col=None, parse_dates=[0]) 
gf


# GO 141  EQU CO2 um/m
folder_name='GO_pCO2'
_col = 'CO2 um/m'
_type ='EQU'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom03'+'/'+'go141_pco2_equ_10min.csv'
dg=pd.read_csv(_file, index_col=None, parse_dates=[0]) 

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/'+'anom03'+'/'+'gps_go141_pco2_equ_10min.csv'
gps.merge(dg[['UTC', _col]], how='inner', on='UTC').dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')

gf=pd.read_csv(_file, index_col=None, parse_dates=[0]) 
gf




