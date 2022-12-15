import pandas as pd
import plotly.express as px
# us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

cruise='ARA12B'

# GO 141  ATM CO2 um/m
folder_name='GO_pCO2'
_col='CO2 um/m'
_type='ATM'
_file='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom01/gps_go141_pco2_atm_1min.csv'
df = pd.read_csv(_file)



fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 um/m", hover_data=["UTC", "Latitude", "Longitude", "CO2 um/m"],
                        zoom=2, height=700)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

px.set_mapbox_access_token(open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read())


fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 um/m", hover_data=["UTC", "Latitude", "Longitude", "CO2 um/m"],
                        zoom=2, height=700)
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="dark")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, hovermode="closest")

fig.show()




fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 um/m", hover_data=["UTC", "Latitude", "Longitude", "CO2 um/m"],
                        zoom=0, height=200, width=300, center=dict(lat=72, lon=-172.5))
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 um/m", hover_data=["UTC", "Latitude", "Longitude", "CO2 um/m"],
                        zoom=2, height=350, width=375, center=dict(lat=74, lon=-172.5))
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

folder_name='GO_pCO2'
fname='co2_in_air_map.html'
# fname=input('fname = ')
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  