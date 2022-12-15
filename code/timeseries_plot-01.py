import datetime
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates
import plotly.express as px 
import os

# Hovermode closest (default mode)
def plot_html(df: pd.DataFrame, _file):
    fig = px.line(df, x="UTC", y=_col, markers=True)
    # fig = px.scatter(days, x="UTC", y=_col)
    fig.update_traces(marker_size=5, marker_color='blue', line_color='red', line_width =3, marker_opacity=0.25)
    # fig.update_traces(marker_size=5, marker_opacity=0.25)
    fig.write_html(_file)
    fig.show()  

# Hovermode closest (default mode) + hover_data
def plot_html_hover_lon_lat(df: pd.DataFrame, _file):
    fig = px.line(df, x="UTC", y=_col, markers=True, hover_data=['UTC', 'Longitude', 'Latitude', _col])
    fig.update_traces(marker_size=5, marker_color='blue', line_color='red', line_width =3, marker_opacity=0.25)
    fig.write_html(_file)
    fig.show()  



def plot_html_hovermode_x(df: pd.DataFrame, _file):
    fig = px.line(df, x="UTC", y=_col, markers=True)
    # fig = px.scatter(days, x="UTC", y=_col)
    fig.update_traces(marker_size=5, marker_color='blue', line_color='red', line_width =3, marker_opacity=0.25, hovertemplate=None)
    fig.update_layout(hovermode="x")
    fig.write_html(_file)
    fig.show()    

def plot_html_hovermode_unified(df: pd.DataFrame, _file):
    fig = px.line(df, x="UTC", y=_col, markers=True)
    # fig = px.scatter(days, x="UTC", y=_col)
    fig.update_traces(marker_size=5, marker_color='blue', line_color='red', line_width =3, marker_opacity=0.25, hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    fig.write_html(_file)
    fig.show()         



cruise = 'ARA12B'

### 10 min average, ARA12B
# d1 = '2021-07-20 12:00:00'
# d2 = '2021-08-18 12:00:00'


folder_name = 'GO_pCO2'

### flux 
print('flux')
fname = 'lon_lat_flux_10min_ara12b.csv'
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+fname

_col = u'flux(mmol/m2/day)_W14'

cf = pd.read_csv(_file, parse_dates=[0])
cf.rename(columns={'Unnamed: 0':'UTC'}, inplace=True)

fname = 'flux_10min_ara12b.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
plot_html(cf[['UTC',_col]], _file)

fname = 'flux_10min_ara12b_hover_lon_lat.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
plot_html_hover_lon_lat(cf, _file)

fname = 'flux_10min_ara12b_hovermode_x.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
plot_html_hovermode_x(cf[['UTC',_col]], _file)

fname = 'flux_10min_ara12b_hovermode_unified.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
plot_html_hovermode_unified(cf[['UTC',_col]], _file)


# co2 in air
print('co2 in air')
fname = 'lon_lat_co2_air_10min_ara12b.csv'
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+fname

_col = u'CO2 (ppm)'

cf = pd.read_csv(_file, parse_dates=[0])
cf.rename(columns={'Unnamed: 0':'UTC'}, inplace=True)
fname = 'co2_air_10min_ara12b.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
plot_html(cf[['UTC',_col]], _file)


# co2 in seawater
print('co2 in seawater')
fname = 'lon_lat_co2_seawater_10min_ara12b.csv'
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+fname

_col = u'CO2 (ppm)'

cf = pd.read_csv(_file, parse_dates=[0])
cf.rename(columns={'Unnamed: 0':'UTC'}, inplace=True)
fname = 'co2_seawater_10min_ara12b.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
plot_html(cf[['UTC',_col]], _file)


### flux, co2 in air/seawater, wind
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fname = 'co2_gps_sic_ts_wind_flux_10min_ara12b.csv'
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+fname

cf = pd.read_csv(_file, parse_dates=[0])
cf.rename(columns={'Unnamed: 0':'UTC'}, inplace=True)

df = cf.set_index('UTC')

fig1 = px.line(df[['flux(mmol/m2/day)_W14']])
fig2 = px.line(df[['CO2_atm', 'CO2_sw']])
# fig3 = px.line(df['SIC (%)'])
# fig4 = px.line(df['SST SBE45'])
# fig5 = px.line(df[['SSS']])
fig6 = px.line(df[['Wind@10m (m/s)']])
# fig7 = px.line(df['[VTG] SOG (knots)'])
# fig8 = px.line(df[['Longitude', 'Latitude']])

fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

for d in fig1.data:
    fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'],  name = d['name'])), row=1, col=1)
       
for d in fig2.data:
    fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'],  name = d['name'])), row=2, col=1)

# for d in fig3.data:
#     fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'], name = d['name'])), row=3, col=1)

# for d in fig4.data:
#     fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'],  name = d['name'])), row=4, col=1)
       
# for d in fig5.data:
#     fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'],  name = d['name'])), row=5, col=1)

for d in fig6.data:
    fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'], name = d['name'])), row=3, col=1)    

# for d in fig7.data:
#     fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'],  name = d['name'])), row=7, col=1)

# for d in fig8.data:
#     fig.add_trace((go.Scatter(mode='lines+markers', x=d['x'], y=d['y'], name = d['name'])), row=3, col=1)        

fig.update_traces(marker_size=7, line_width =2, marker_opacity=0.25)    
fname = 'flux_co2_air_sw_wind.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  



