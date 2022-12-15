import datetime
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates
import plotly.express as px 
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_html(df: pd.DataFrame, _file):
    fig = px.line(df, x="UTC", y=_col, markers=True)
    # fig = px.scatter(days, x="UTC", y=_col)
    fig.update_traces(marker_size=5, marker_color='blue', line_color='red', line_width =3, marker_opacity=0.25)
    # fig.update_traces(marker_size=5, marker_opacity=0.25)
    fig.write_html(_file)
    fig.show()  



cruise = 'ARA12B'
folder_name = 'GO_pCO2'

### flux, co2 in air/seawater, wind
###  timeseries plot
fname = 'lon_lat_flux_10min_ara12b.csv'
_file = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+fname

_col = u'flux(mmol/m2/day)_W14'
cf = pd.read_csv(_file, parse_dates=[0])
cf.rename(columns={'Unnamed: 0':'UTC'}, inplace=True)

# fig.add_trace(go.Scatter(x=cf['UTC'], y=cf[_col], name=_col), row=1, col=2)

# fig.update_layout(legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
# ))

# fig.update_layout(showlegend=False)

# fig.update_layout(
#     mapbox = {
#         'accesstoken': token,
#         'style': "outdoors", 'zoom': 0.7},
#     showlegend = False)

# fig.update_annotations(dict(font_size=8))
# for col in [1, 2]:
#     fig.add_annotation(dict(x=col / 2 - 0.4, y=0.8, xref="paper", yref="paper", 
#                             text=_col, showarrow=False))









