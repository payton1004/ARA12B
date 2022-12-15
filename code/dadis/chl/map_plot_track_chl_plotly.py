import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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

px.set_mapbox_access_token(open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read())
   
# fig = px.scatter_mapbox(af, lat="lat", lon="lon", color =_col, hover_data=["UTC", _col, "lat", "lon"],
#                         zoom=1.7, height=350, width=400, color_continuous_scale=px.colors.sequential.Jet, center=dict(lat=74, lon=187.5))     
# # fig = px.scatter_mapbox(sf, lat="lat", lon="lon", hover_data=["lat", "lon", "Station No."], color='remark',
# #                         zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))                                                                     
# fig.update_layout(mapbox_style="satellite")
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.update_traces(marker={'size': 3.0})
# fig.update_layout(hovermode='closest')

# folder_name='DaDis'
# _dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
# fname='map_chl_jet.html'
# fig.write_html(_dir+fname)
# fig.show()  


fig = px.scatter_mapbox(af, lat="lat", lon="lon", color =_col, hover_data=["UTC", _col, "lat", "lon"],
                        zoom=1.7, height=350, width=400,     color_continuous_scale=[(0.0, '#1a1a1a'),((8.3-af[_col].min())/(af[_col].max()-af[_col].min()), '#1a1a1a'),
                            ((8.3-af[_col].min())/(159.297235-af[_col].min()), '#4575b4'), ((9.1-af[_col].min())/(af[_col].max()-af[_col].min()), '#4575b4'),
                            ((9.1-af[_col].min())/(af[_col].max()-af[_col].min()), '#74add1'), ((9.5-af[_col].min())/(af[_col].max()-af[_col].min()), "#74add1"),
                            ((9.5-af[_col].min())/(af[_col].max()-af[_col].min()), '#abd9e9'), ((9.8-af[_col].min())/(af[_col].max()-af[_col].min()), "#abd9e9"),
                            ((9.8-af[_col].min())/(af[_col].max()-af[_col].min()), '#e0f3f8'), ((10.1-af[_col].min())/(af[_col].max()-af[_col].min()), "#e0f3f8"),
                            ((10.1-af[_col].min())/(af[_col].max()-af[_col].min()), '#fee090'), ((10.6-af[_col].min())/(af[_col].max()-af[_col].min()), "#fee090"),
                            ((10.6-af[_col].min())/(af[_col].max()-af[_col].min()), '#fdae61'), ((11.3-af[_col].min())/(af[_col].max()-af[_col].min()), "#fdae61"),
                            ((11.3-af[_col].min())/(af[_col].max()-af[_col].min()), '#f46d43'), ((13.3-af[_col].min())/(af[_col].max()-af[_col].min()), "#f46d43"),
                            ((13.3-af[_col].min())/(af[_col].max()-af[_col].min()), '#d73027'), ((17.6-af[_col].min())/(af[_col].max()-af[_col].min()), "#d73027"),
                            ((17.6-af[_col].min())/(af[_col].max()-af[_col].min()), '#67001f'),  (1.00, '#67001f')], center=dict(lat=74, lon=187.5))     
# fig = px.scatter_mapbox(sf, lat="lat", lon="lon", hover_data=["lat", "lon", "Station No."], color='remark',
#                         zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))                                                                     
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_traces(marker={'size': 3.0})
fig.update_layout(hovermode='closest')

folder_name='DaDis'
_dir = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+subfolder_name+'/'+'chl'+'/'
fname='map_chl_cb_10_RdYlBu.html'
fig.write_html(_dir+fname)
# fig.show()  







