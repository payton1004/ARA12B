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
df = df.round({'Longitude': 2, 'Latitude': 2, 'CO2 (ppm)': 2})


token = open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read() # you will need your own token
# px.set_mapbox_access_token(open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read())

# fig = make_subplots(
#     rows=1, cols=2,
#     # column_widths=[0.38,0.6],
#     column_widths=[0.4,0.6],
#     # row_heights=[1],
#     specs=[[{"type": "mapbox"}, {"type": "xy"}]]
#     )   

# fig = make_subplots(
#     rows=2, cols=2,
#     column_widths=[0.4, 0.6],
#     row_heights=[0.4, 0.6],
#     specs=[[{"type": "mapbox", "rowspan": 2}, {"type": "xy"}],
#            [            None                    , {"type": "table"}]])        
fig = make_subplots(
    rows=2, cols=2,
    column_widths=[0.4, 0.6],
    row_heights=[0.6, 0.4],
    vertical_spacing=0.03,
    specs=[[{"type": "mapbox", "rowspan": 2}, {"type": "table"}],
           [            None                    , {"type": "xy"}]])                    

fig.add_trace(
    go.Scattermapbox(lat=df["Latitude"], 
    lon=df["Longitude"], 
    # mode='text', 
    mode='markers',
    marker=dict(size=4, 
    showscale=True,
    colorscale='Turbo',
    # colorbar=dict(x=0.35),
    colorbar=dict(x=-0.1),
    color=df[_col]),
    name=_col,
    # legendgrouptitle='',
    # hoverlabel='',
    # hoverinfo=''
    # hovertemplate="CO2 (ppm): %{_col:$.2f}",
    # hovertemplate="%{_col:$.2f}",
    hovertext=df[[_col, 'UTC']],
    # hovertext=df[_col],
    showlegend=False
    ),
    row=1, col=1
)

fig.add_trace(go.Scatter(x=df['UTC'], 
                         y=df[_col], 
                        #  name=_col, 
                         mode='lines+markers',
                         marker=dict(size=7, 
                         color='blue',
                         opacity=0.5
                         ),
                         line=dict(color='red',
                                   width=2
                         ),
                         name=_col,
                        #  hovertext=df['Longitude'],
                        #  hovertext=df['Latitude'],
                         hovertext=df[['Latitude', 'Longitude']],
                         showlegend=False), 
                    row=2, col=2)
fig.update_layout(
    yaxis_title="CO2 (ppm)",
)

fig.add_trace(
    go.Table(
        header=dict(
            values=["UTC", "Longitude", "Latitude", "CO2 (ppm)"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[df[k].tolist() for k in df.columns[:]],
            align = "left")
    ),
    row=1, col=2
)



fig.update_layout(
    title="CO2 (ppm) in air during ARA12B",
    # xaxis_title="X Axis Title",
    # yaxis_title="CO2 (ppm)",
    # legend_title="Legend Title",
    # font=dict(
    #     family="Courier New, monospace",
    #     size=18,
    #     color="RebeccaPurple"
    # )
)


fig.update_layout(
    autosize=True,
    hovermode='x unified'
    # hovermode='closest'
    )

fig.update_mapboxes(
        bearing=0,
        accesstoken=token,
        center=dict(
            lon=-172.5,
            lat=74
        ),
        # pitch=0,
        style="satellite",
        zoom=2.7)
# fig.update_layout(mapbox_style="satellite")


folder_name='GO_pCO2'
fname='mapbox_xy_table.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  





