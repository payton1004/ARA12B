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

# cruise = 'ARA12A'
cruise = 'ARA12B'
d1 = '2021-07-01 00:00:00'
# d2 = '2021-07-21 23:59:59'
# d1 = '2021-07-20 12:00:00'
d2 = '2021-08-18 12:00:00'


# GPS
folder_name = 'DaDiS'
df=pd.read_csv('/Users/jung-ok/work1/ARA12B/processed/DaDiS/GPS/GPS_1sec.csv', index_col=None, parse_dates=[0]) 

df.rename(columns={'UTC Time':'UTC'}, inplace=True)
# ['UTC', 'Latitude', 'Longitude']
gps = df[['UTC', 'Latitude', 'Longitude']][(df.UTC >=d1) & (df.UTC <=d2)]

# _file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+'utc_lon_lat_1sec.csv'
# gps.dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')




# HydroC pCO2_corr
folder_name='HydroC_pCO2'
# _col = 'pCO2_corr'
_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+'HydroC_pCO2_all.csv'
# _file = '/Users/jung-ok/work1/ARA12B/processed/HydroC_pCO2/HydroC_pCO2_all.csv'
dg=pd.read_csv(_file, index_col=None, parse_dates=[0]) 

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+'utc_lat_lon_hydroc_pco2.csv'
# gps.merge(dg[['UTC', _col]], how='inner', on='UTC').dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')
gps.merge(dg, how='inner', on='UTC').dropna().to_csv(_file, na_rep=np.nan, index=False, float_format='%g')
gf=pd.read_csv(_file, index_col=None, parse_dates=[0]) 
# gf




