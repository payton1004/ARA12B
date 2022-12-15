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
_d = '2021-07-24 00:00'

# HydroC pCO2_corr

folder_name='HydroC_pCO2'
print(folder_name)
_col = 'pCO2_corr'
_ylabel = '$p$CO$_2$ [$\mu$atm]'


_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/anom03/'+'gps_hydroc_pco2_10min.csv'
# dg.dropna().to_csv(_file, na_rep=np.nan, index=True, float_format='%g')

dg=pd.read_csv(_file, parse_dates=True, index_col=[0])


print("all")
# dg.describe()
print("average: {:.2f}".format(dg[_col].mean()))
print("standard deviation:{:.2f}".format(dg[_col].std()))
print("")
print("before seaice")
db = dg[(dg.index < _d)]
# print("Longitude: {:.2f}".format(db['Longitude'][-1]))
# print("Latitude: {:.2f}".format(db['Latitude'][-1]))
# db[_col].plot()
# plt.show()
print("average: {:.2f}".format(db[_col].mean()))
print("standard deviation:{:.2f}".format(db[_col].std()))
print("")
print("after seaice")
da = dg[(dg.index >=_d)]
# print("Longitude: {:.2f}".format(da['Longitude'][0]))
# print("Latitude: {:.2f}".format(da['Latitude'][0]))
# da[_col].plot()
# plt.show()
print("average: {:.2f}".format(da[_col].mean()))
print("standard deviation:{:.2f}".format(da[_col].std()))

print("")
print("")

# GO 141  ATM CO2 um/m
folder_name='GO_pCO2'


_col = 'CO2 um/m'
_ylabel = 'xCO$_2$ [ppm]'
_type ='ATM'

print(folder_name+' '+_type)

_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom01/'+'gps_go141_pco2_atm_1min.csv'

dg=pd.read_csv(_file, parse_dates=True, index_col=[0])


print("all")
# dg.describe()
print("average: {:.2f}".format(dg[_col].mean()))
print("standard deviation:{:.2f}".format(dg[_col].std()))
print("")
print("before seaice")
db = dg[(dg.index < _d)]
# print("Longitude: {:.2f}".format(db['Longitude'][-1]))
# print("Latitude: {:.2f}".format(db['Latitude'][-1]))
# db[_col].plot()
# plt.show()
print("average: {:.2f}".format(db[_col].mean()))
print("standard deviation:{:.2f}".format(db[_col].std()))
print("")
print("after seaice")
da = dg[(dg.index >=_d)]
# print("Longitude: {:.2f}".format(da['Longitude'][0]))
# print("Latitude: {:.2f}".format(da['Latitude'][0]))
# da[_col].plot()
# plt.show()
print("average: {:.2f}".format(da[_col].mean()))
print("standard deviation:{:.2f}".format(da[_col].std()))



print("")
print("")
# GO 141  EQU CO2 um/m
folder_name='GO_pCO2'
# print(folder_name)
_col = 'CO2 um/m'
_ylabel = 'xCO$_2$ [ppm]'
_type ='EQU'
print(folder_name+' '+_type)


_file ='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom03/'+'gps_go141_pco2_equ_10min.csv'

dg=pd.read_csv(_file, parse_dates=True, index_col=[0])


print("all")
# dg.describe()
print("average: {:.2f}".format(dg[_col].mean()))
print("standard deviation:{:.2f}".format(dg[_col].std()))
print("")
print("before seaice")
db = dg[(dg.index < _d)]
# print("Longitude: {:.2f}".format(db['Longitude'][-1]))
# print("Latitude: {:.2f}".format(db['Latitude'][-1]))
# db[_col].plot()
# plt.show()
print("average: {:.2f}".format(db[_col].mean()))
print("standard deviation:{:.2f}".format(db[_col].std()))
print("")
print("after seaice")
da = dg[(dg.index >=_d)]
# print("Longitude: {:.2f}".format(da['Longitude'][0]))
# print("Latitude: {:.2f}".format(da['Latitude'][0]))
# da[_col].plot()
# plt.show()
print("average: {:.2f}".format(da[_col].mean()))
print("standard deviation:{:.2f}".format(da[_col].std()))

