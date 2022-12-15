# Fluorescence
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
from datetime import timedelta
import os
import functools
from matplotlib import dates

cruise = 'ARA12B'

folder_name='DaDis'
sensor = 'Fluorometer'


files = sorted(glob.glob('/Users/jung-ok/work1/'+cruise+'/raw_data/'+folder_name+'/'+sensor+'/FM*.dat'))
# files = glob('/work1/ARA12B/raw_data/DaDiS/Flu*/FM-2019*.dat')

old_folder='/Users/jung-ok/work1/'+cruise+'/raw_data/'+folder_name+'/'+sensor+'/'
new_folder='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+sensor+'/'

fname='FM_all.csv'
g = open(new_folder+fname, 'w')
# g = open('/work1/ARA12B/processed/DaDiS/ARA12B_FM_all.csv', 'w')
g.write('UTC,Longitude,Latitude,Fluorescence,SST\n')

for fname in files:
    f = open(fname, 'r')
#     print fname
    for fLine in f.readlines()[2:]:
        try:
            fs = fLine.split(',')
            if len(fs) >= 6:
                #UTC
                udate = datetime.datetime.strptime(fs[0], '%Y%m%d')
                utime = datetime.datetime.strptime(fs[1], '%H%M%S.00')
                utc = datetime.datetime(udate.year, udate.month, udate.day, utime.hour, utime.minute, utime.second)
                utc_str = utc.strftime('%Y-%m-%dT%H:%M:%S')
                #Coordinates
                lat_deg, lat_min = float(fs[2])//100, float(fs[2])%100
                lat = lat_deg + lat_min / 60
                if 'S' in fs[3]:
                    lat = -1 * lat
                lon_deg, lon_min = float(fs[4])//100, float(fs[4])%100
                lon = lon_deg + lon_min / 60
                if 'W' in fs[5]:
                    lon = -1 * lon
                fluorescence, sst = float(fs[6]), float(fs[7])
                gLine = '%s,%8.4f,%8.4f,%7.4f,%7.4f\n' % (utc_str,lon,lat,fluorescence,sst)
                g.write(gLine)
        except:
            continue
    f.close()
    
g.close()