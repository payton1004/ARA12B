import pandas as pd
import numpy as np

_dir='/Users/jung-ok/work1/ARA12B/stationinfo/'
# fname='ARA12B_stationinfo_20210731.xlsx'
fname='ARA12B_stationinfo_20210814.xlsx'
df = pd.read_excel(open(_dir+fname,'rb'))
print(df.info())
# >>> df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 95 entries, 0 to 94
# Data columns (total 43 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   Expedition     98 non-null     object 
#  1   Leg            98 non-null     object 
#  2   Station No.    98 non-null     object 
#  3   St. Full Name  98 non-null     object 
#  4   Lat_Deg        98 non-null     float64
#  5   Lat_Min        98 non-null     float64
#  6   Long_Deg       98 non-null     float64
#  7   Long_Min       98 non-null     float64
#  8   Lat_Deg10      98 non-null     float64
#  9   Long_Deg10     98 non-null     float64
#  10  Depth(m)       98 non-null     float64
#  11  No. of Work    99 non-null     float64
#  12  Work01_Gear    103 non-null    object 
#  13  Work01_Hour    104 non-null    float64
#  14  Work02_Gear    57 non-null     object 
#  15  Work02_Hour    58 non-null     float64
#  16  Work03_Gear    54 non-null     object 
#  17  Work03_Hour    55 non-null     float64
#  18  Work04_Gear    48 non-null     object 
#  19  Work04_Hour    49 non-null     float64
#  20  Work05_Gear    46 non-null     object 
#  21  Work05_Hour    47 non-null     float64
#  22  Work06_Gear    45 non-null     object 
#  23  Work06_Hour    46 non-null     float64
#  24  Work07_Gear    32 non-null     object 
#  25  Work07_Hour    31 non-null     float64
#  26  Work08_Gear    24 non-null     object 
#  27  Work08_Hour    24 non-null     float64
#  28  Work09_Gear    20 non-null     object 
#  29  Work09_Hour    20 non-null     float64
#  30  Work10_Gear    14 non-null     object 
#  31  Work10_Hour    14 non-null     float64
#  32  Work11_Gear    9 non-null      object 
#  33  Work11_Hour    9 non-null      float64
#  34  Work12_Gear    3 non-null      object 
#  35  Work12_Hour    3 non-null      float64
#  36  Work13_Gear    2 non-null      object 
#  37  Work13_Hour    2 non-null      float64
#  38  Work14_Gear    2 non-null      object 
#  39  Work14_Hour    2 non-null      float64
#  40  Work15_Gear    0 non-null      float64
#  41  Work15_Hour    0 non-null      float64
#  42  Total_Hour     98 non-null     float64


### using dictionary to convert specific columns 
# convert_dict = {'Long_Deg10': float, 
#                 'Lat_Deg10': float, 
#                 'Station No.': str
#                 }                                   
# df = df.astype(convert_dict) 


_dir='/Users/jung-ok/work1/ARA12B/stationinfo/'
# fname='ARA12B_long_lat_station_20210731.csv'
fname='ARA12B_long_lat_station_20210814.csv'
df[['Long_Deg10', 'Lat_Deg10', 'Station No.', 'No. of Work']][:].to_csv(_dir+fname, index=False, na_rep=np.nan, float_format='%g')


# _dir='/Users/jung-ok/work1/ARA12B/stationinfo/'
# fname='ARA12B_station_lat_long_20210727.csv'
# df = pd.read_csv(_dir+fname, index_col=None)
