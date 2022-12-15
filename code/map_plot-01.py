import pandas as pd
import plotly.express as px

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

# fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 um/m", hover_data=["UTC", "Latitude", "Longitude", "CO2 um/m"],
#                         zoom=2, height=350, width=375, center=dict(lat=74, lon=-172.5))
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 (ppm)", hover_data=["UTC", "Latitude", "Longitude", "CO2 (ppm)"],
                        zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

folder_name='GO_pCO2'
fname='co2_in_air_map.html'
# fname=input('fname = ')
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  

# GO 141 EQU CO2 um/m
_type='EQU'
# _file='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+_type+'/anom03/gps_go141_pco2_equ_10min.csv'
_file='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+'lon_lat_co2_seawater_10min_ara12b.csv'
df = pd.read_csv(_file)
df.rename(columns={'Unnamed: 0':'UTC'}, inplace=True)

# fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 um/m", hover_data=["UTC", "Latitude", "Longitude", "CO2 um/m"],
#                         zoom=2, height=350, width=375, center=dict(lat=74, lon=-172.5))
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="CO2 (ppm)", hover_data=["UTC", "Latitude", "Longitude", "CO2 (ppm)"],
                        zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))                        
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

folder_name='GO_pCO2'
fname='co2_in_seawater_map.html'
# fname=input('fname = ')
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  

# GO 141 CO2 flux mmol/m2/day
_file='/Users/jung-ok/work1/'+cruise+'/processed/'+folder_name+'/'+'lon_lat_flux_10min_ara12b.csv'
df = pd.read_csv(_file)
df.rename(columns={'Unnamed: 0':'UTC', 'flux(mmol/m2/day)_W14':'flux(mmol/m2/day)'}, inplace=True)

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color ="flux(mmol/m2/day)", hover_data=["UTC", "Latitude", "Longitude", "flux(mmol/m2/day)"],
                        zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))                        
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

folder_name='GO_pCO2'
fname='flux_map.html'
# fname=input('fname = ')
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  

