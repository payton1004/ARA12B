import gdown
import pandas as pd
import matplotlib.pyplot as plt
import glob
import datetime

import numpy as np

cruise = 'ARA12B'

# GO 141 pCO2 system data

folder_name='GO_pCO2'
# folder_name=input('folder_name = ')
fname='GO_pCO2_all.csv'
# fname=input('fname = ')
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+fname
# dg=pd.read_csv(_file, index_col=[0], parse_dates=True)
# _type = 'EQU'
# _type = 'ATM'
_type = input('_type = ')

# dg=dg[dg['Type'].str.replace(' ', '')==_type]


# fname='GO_pCO2_all_'+_type+'_10min.csv'
# # fname=input('fname = ')
# _file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+fname
# # df.drop('b', axis=1)
# dg.drop('Type', axis=1).resample('10min').mean().to_csv(_file, na_rep=np.nan)


df = pd.read_csv(_file, parse_dates=[0])
df=df[df['Type'].str.replace(' ', '')==_type].sort_values(by='UTC', ascending=True)


def plot_date(day: str, df: pd.DataFrame):
    day1 = df[
        (df["UTC"] >= f"{day} 00:00:00")
        & (df["UTC"] <= f"{day} 23:00:00")
    ]
    day1.set_index("UTC").plot()
    plt.show()


_col = 'CO2 um/m'
_type = 'EQU'
# _type = input('_type = ')
    
# plot_date("2021-07-26", df[['UTC',_col]][df['Type'].str.replace(' ', '')==_type])
# plot_date("2021-07-26", df[['UTC',_col]])

for _day in pd.date_range(start='7/11/2021', end='8/18/2021'):
    # print(_day.strftime('%Y-%m-%d'))
    # plot_date(_day, df[['UTC',_col]][df['Type'].str.replace(' ', '')==_type])
    plot_date(_day, df[['UTC',_col]])

from kats.consts import TimeSeriesData

# Construct TimeSeriesData object
# df = df[['UTC',_col]][df['Type'].str.replace(' ', '')==_type].rename(columns={"UTC": "time", "CO2 um/m":"value"})
df = df[['UTC',_col]].rename(columns={"UTC": "time", "CO2 um/m":"value"})
# df = df[['UTC',_col]][df['Type'].str.replace(' ', '')==_type].rename(columns={"UTC": "time"})

df = df[(df['time']>='2021-08-10')&(df['time']<='2021-08-14')]
ts = TimeSeriesData(df)
# ts = TimeSeriesData(df.dropna(subset=['CO2 um/m']))
# ts = TimeSeriesData(df.dropna())




from kats.utils.decomposition import TimeSeriesDecomposition

decomposer = TimeSeriesDecomposition(ts, decomposition="additive")
# # decomposer = TimeSeriesDecomposition(ts, decomposition="multiplicative")


results = decomposer.decomposer()


fig = decomposer.plot()
plt.show()


def plot_season_in_a_day(day: str, seasonal: pd.DataFrame):
    day1 = seasonal[
        (seasonal.time >= f"{day} 00:00:00") & (seasonal.time <= f"{day} 23:00:00")
    ]
    day1.plot(cols=["season"])
    plt.show()


plot_season_in_a_day("2021-07-10", results["seasonal"])
plot_season_in_a_day("2021-08-02", results["seasonal"])
plot_season_in_a_day("2021-08-10", results["seasonal"])


from kats.detectors.seasonality import FFTDetector

fft_detector = FFTDetector(ts)
fft_detector.detector()

# Detect Change Point
# CUSUMDetector — Detect an Up/Down Shift of Means

# url = "https://drive.google.com/uc?id=1i1Yz3-rfjuemc7bD1IXpvb7c1kTOw09b"
# output = "google-analytics-20210101-20210802-days.csv"
# gdown.download(url, output)

# day_df = pd.read_csv(
#     "google-analytics-20210101-20210802-days.csv", parse_dates=["Day Index"]
# )

day_df = pd.read_csv(_file, parse_dates=['UTC'])

# day_df = day_df[['UTC',_col]][day_df['Type'].str.replace(' ', '')==_type]
day_df = day_df[['UTC',_col]]


import plotly.express as px 

fig = px.line(day_df, x="UTC", y=_col)
fig.show()

import numpy as np
from kats.consts import TimeSeriesData

# convert to TimeSeriesData object
day_df.rename(columns={'UTC':'time'}, inplace=True)
ts_day = TimeSeriesData(day_df)



from kats.detectors.cusum_detection import CUSUMDetector
# cumsum_detector = CUSUMDetector(timeseries)
cumsum_detector = CUSUMDetector(ts_day)
changepoints = cumsum_detector.detector()
print(changepoints[0][0])

# Plot
cumsum_detector.plot(changepoints)
plt.show()


from kats.detectors.bocpd import BOCPDetector, BOCPDModelType, TrendChangeParameters

bocpd_detector = BOCPDetector(ts_day)

changepoints = bocpd_detector.detector(
    model=BOCPDModelType.NORMAL_KNOWN_MODEL, changepoint_prior=0.01
)

for changepoint in changepoints:
    print(changepoint[0])
    
# Plot
bocpd_detector.plot(changepoints)
plt.show()

from kats.detectors.outlier import OutlierDetector

outlier_detector = OutlierDetector(ts_day, "additive")

outlier_detector.detector()
outliers = outlier_detector.outliers
outliers[0]


ts_day_outliers_interpolated = outlier_detector.remover(interpolate=True)
from matplotlib import pyplot as plt

# ax = ts_day.to_dataframe().plot(x="time", y="value")
ax = ts_day.to_dataframe().plot(x="time", y="CO2 um/m")
ts_day_outliers_interpolated.to_dataframe().plot(x="time", y="y_0", ax=ax)
plt.legend(labels=["original ts", "ts with removed outliers"])
plt.show()