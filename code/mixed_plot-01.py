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


cruise='ARA12B'

# GO 141  ATM CO2 um/m
folder_name='GO_pCO2'
# _col='CO2 um/m'
_col='CO2 (ppm)'

_type='ATM'
# _file='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom01/gps_go141_pco2_atm_1min.csv'
_file='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+'lon_lat_co2_air_10min_ara12b.csv'
df = pd.read_csv(_file)
df.rename(columns={'Unnamed: 0':'UTC'}, inplace=True)

# token = open(".mapbox_token").read() # you will need your own token
px.set_mapbox_access_token(open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read())


fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 (ppm)", hover_data=["UTC", "Latitude", "Longitude", "CO2 (ppm)"],
                        zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

folder_name='GO_pCO2'
fname='co2_in_air_map.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  


# Initialize figure with subplots
# fig = make_subplots(
#     rows=2, cols=2,
#     column_widths=[0.5,0.5],
#     # row_heights=[1],
#     specs=[[{"type": "scattergeo", "rowspan": 2}, {"type": "xy", "rowspan": 2}],
#     [None, None]
#     ])

# fig = make_subplots(
#     rows=2, cols=2,
#     column_widths=[0.5,0.5],
#     # row_heights=[1],
#     specs=[[{"type": "mapbox", "rowspan": 2}, {"type": "xy", "rowspan": 2}],
#     [None, None]
#     ])    

token = open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read() # you will need your own token
# px.set_mapbox_access_token(open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read())

fig = make_subplots(
    rows=1, cols=2,
    # column_widths=[0.38,0.6],
    column_widths=[0.4,0.6],
    # row_heights=[1],
    specs=[[{"type": "mapbox"}, {"type": "xy"}]]
    )        

fig.add_trace(
    go.Scattermapbox(lat=df["Latitude"], 
    lon=df["Longitude"], 
    mode='markers', 
    marker=dict(size=4, 
    showscale=True,
    colorscale='Turbo',
    # colorbar=dict(x=0.35),
    colorbar=dict(x=-0.1),
    color=df[_col]),
    showlegend=False,
    name=_col,
    # legendgrouptitle='',
    # hoverlabel='',
    # hoverinfo=''
    hovertext=df[_col]
    ),
    row=1, col=1
)

fig.add_trace(go.Scatter(x=df['UTC'], y=df[_col], name=_col, showlegend=False), row=1, col=2)
fig.update_layout(
    yaxis_title="CO2 (ppm)",
)

fig.update_layout(
    autosize=True,
    hovermode='closest')

fig.update_mapboxes(
        # bearing=0,
        accesstoken=token,
        center=dict(
            lon=-172.5,
            lat=74
        ),
        # pitch=0,
        zoom=2)
fig.update_layout(mapbox_style="satellite")
folder_name='GO_pCO2'
fname='mixed_scattermapbox.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  


# token = open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read() # you will need your own token

# fig = make_subplots(
#     rows=1, cols=2,
#     column_widths=[0.4,0.6],
#     # row_heights=[1],
#     specs=[[{"type": "scattergeo"}, {"type": "xy"}]]
#     )        

# fig.add_trace(
#     go.Scattergeo(lat=df["Latitude"], lon=df["Longitude"], mode='markers', showlegend=False, marker=dict(size=4)),
#     row=1, col=1
# )

# fig.add_trace(go.Scatter(x=df['UTC'], y=df[_col], name=_col), row=1, col=2)

# fig.update_layout(
#     yaxis_title="CO2 (ppm)",
# )


# fig.update_layout(
#     autosize=True,
#     hovermode='closest')

# fig.update_layout(showlegend=False)

# # Update geo subplot properties
# fig.update_geos(
#     # projection_type="orthographic",
#     # landcolor="white",
#     # oceancolor="MidnightBlue",
#     # showocean=True,
#     # lakecolor="LightBlue",
#     center=dict(
#     lat=74,
#     lon=-172.5)
# )

# fig.update_geos(fitbounds="locations")
# # fig.update_geos(resolution="50")
# # fig.update_geos(scope="asia")

# folder_name='GO_pCO2'
# fname='mixed_scattergeo.html'
# _file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
# fig.write_html(_file)
# fig.show()  


# import plotly.graph_objects as go
# fig = go.Figure()

# fig.add_trace(
#     go.Scattermapbox(
#         lat=['45.5017'],
#         lon=['-73.5673'],
#         mode='markers',
#         marker=dict(
#             size=14
#         ),
#         text=['Montreal'],
#         subplot='mapbox',
#     ))
# fig.add_trace(  
#     go.Scattermapbox(
#         lat=['45.5017'],
#         lon=['-73.5673'],
#         mode='markers',
#         marker=dict(
#             size=14
#         ),
#         text=['Montreal'],
#         subplot='mapbox2',
#     ))

# fig.update_layout(
#     autosize=True,
#     hovermode='closest',
#     mapbox=dict(
#         style='open-street-map',
#         domain={'x': [0, 0.4], 'y': [0, 1]},
#         bearing=0,
#         center=dict(
#             lat=45,
#             lon=-73
#         ),
#         pitch=0,
#         zoom=5
#     ),
#         mapbox2=dict(
#         style='open-street-map',
#         domain={'x': [0.6, 1.0], 'y': [0, 1]},
#         bearing=0,
#         center=dict(
#             lat=45,
#             lon=-73
#         ),
#         pitch=0,
#         zoom=5
#     ),
# )
# fig.show()



