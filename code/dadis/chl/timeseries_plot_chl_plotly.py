import datetime
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates, mathtext
import plotly.express as px 
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

cruise='ARA12B'

# DaDis Fluorometer data
folder_name = 'DaDis'
subfolder_name = 'Fluorometer'

_col = 'Fluorescence'

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'FM_all_filter_chl_10min_mean.csv'
df = pd.read_csv(_dir+fname)

af = df[['UTC', 'Longitude, mean', 'Latitude, mean', 'Fluorescence, mean', 'Fluorescence, std', 'Fluorescence, count']].dropna()
af.rename(columns={'Longitude, mean':'lon', 'Latitude, mean':'lat', 'Fluorescence, mean':_col}, inplace=True)

_dir = '/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname = 'utc_lon_lat_chl_10min_mean.csv'
af.to_csv(_dir+fname, index=False, na_rep='NaN')

# 10 8.3
# 20 9.1 
# 30 9.5
# 40 9.8
# 50 10.1
# 60 10.6
# 70 11.3
# 80 13.3
# 90 17.6
      
fig = px.scatter(af, x="UTC", y=_col, color=_col, \
    color_continuous_scale=[(0.0, '#1a1a1a'),((8.3-af[_col].min())/(af[_col].max()-af[_col].min()), '#1a1a1a'),
                            ((8.3-af[_col].min())/(159.297235-af[_col].min()), '#4575b4'), ((9.1-af[_col].min())/(af[_col].max()-af[_col].min()), '#4575b4'),
                            ((9.1-af[_col].min())/(af[_col].max()-af[_col].min()), '#74add1'), ((9.5-af[_col].min())/(af[_col].max()-af[_col].min()), "#74add1"),
                            ((9.5-af[_col].min())/(af[_col].max()-af[_col].min()), '#abd9e9'), ((9.8-af[_col].min())/(af[_col].max()-af[_col].min()), "#abd9e9"),
                            ((9.8-af[_col].min())/(af[_col].max()-af[_col].min()), '#e0f3f8'), ((10.1-af[_col].min())/(af[_col].max()-af[_col].min()), "#e0f3f8"),
                            ((10.1-af[_col].min())/(af[_col].max()-af[_col].min()), '#fee090'), ((10.6-af[_col].min())/(af[_col].max()-af[_col].min()), "#fee090"),
                            ((10.6-af[_col].min())/(af[_col].max()-af[_col].min()), '#fdae61'), ((11.3-af[_col].min())/(af[_col].max()-af[_col].min()), "#fdae61"),
                            ((11.3-af[_col].min())/(af[_col].max()-af[_col].min()), '#f46d43'), ((13.3-af[_col].min())/(af[_col].max()-af[_col].min()), "#f46d43"),
                            ((13.3-af[_col].min())/(af[_col].max()-af[_col].min()), '#d73027'), ((17.6-af[_col].min())/(af[_col].max()-af[_col].min()), "#d73027"),
                            ((17.6-af[_col].min())/(af[_col].max()-af[_col].min()), '#67001f'),  (1.00, '#67001f')], 
    hover_data=["lat", "lon"])        
fig.update_traces(mode="markers+lines")

fig.update_traces(marker=dict(opacity=0.5, size=9.0))                               
# fig.update_traces(line={"opacity": 0.2, 
#                           'width': 1.0})     
fig.update_traces(line=dict(width=0.2, color='red'))                        
# fig.update_layout(
#     yaxis_title='SST SBE45 ($^\circ$C)'
# )
fig.update_layout(
    yaxis_title='Chlorophyll-a (ug/L)',
)

fig.update_layout({
'plot_bgcolor': 'rgba(224, 224, 224, 0.5)',
# 'paper_bgcolor': 'rgba(224, 224, 224, 1)',
})

fig.update_layout(
    autosize=True,
    hovermode='x unified'
)

_dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname='timeseries_plot_chl_10min_mean_cb_10_RdYlBu.html'
fig.write_html(_dir+fname)
# fig.show()  

# ### semilogy
# fig = px.scatter(af, x="UTC", y=_col, color=_col, \
#     color_continuous_scale=[(0.00, 'crimson'),   (0.007, 'crimson'),
#                             (0.007, "royalblue"), (0.028, "royalblue"),
#                             (0.028, "mediumseagreen"), (0.037, "mediumseagreen"),
#                             (0.037, "darkorchid"), (0.044, "darkorchid"),
#                             (0.044, "darkorange"), (0.0485, "darkorange"),
#                             (0.0485, "yellow"), (0.058, "yellow"),
#                             (0.058, "saddlebrown"), (0.078, "saddlebrown"),
#                             (0.078, "violet"), (0.15, "violet"),
#                             (0.15, "darkgray"),  (1.00, "darkgray")], 
#     hover_data=["lat", "lon"])        
# fig.update_traces(mode="markers+lines")

# fig.update_traces(marker=dict(opacity=0.5, size=9.0))                               
# # fig.update_traces(line={"opacity": 0.2, 
# #                           'width': 1.0})     
# fig.update_traces(line=dict(width=0.2, color='red'))                        
# # fig.update_layout(
# #     yaxis_title='SST SBE45 ($^\circ$C)'
# # )
# fig.update_layout(
#     yaxis_title='Chlorophyll-a (ug/L)',
# )

# fig.update_layout({
# 'plot_bgcolor': 'rgba(224, 224, 224, 0.5)',
# # 'paper_bgcolor': 'rgba(224, 224, 224, 1)',
# })

# fig.update_layout(
#     autosize=True,
#     hovermode='x unified'
# )

# fig.update_yaxes(type="log")
# fig.update_coloraxes()

# _dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
# fname='timeseries_plot_chl_10min_mean_cb_9_set1_semilogy.html'
# fig.write_html(_dir+fname)
# # fig.show()  

