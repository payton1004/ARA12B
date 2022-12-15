import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

cruise='ARA12B'

# folder_name='DaDis'
# subfolder_name='GPS'

_file='/Users/jung-ok/work1/ARA12B/stationinfo/ARA12B_long_lat_station_20210814.csv'
sf = pd.read_csv(_file)
sf.rename(columns={'Lat_Deg10':'lat', 'Long_Deg10':'lon'}, inplace=True)

sf['remark'] = 'CTD + Other Works'

sf["remark"] = sf["remark"].astype('string') #convert to string
sf['Station No.'] = sf['Station No.'].astype('string')
# sf['Station No.'] = sf['Station No.'].astype(int, errors='ignore')  

# DIC 채수 정점
# No. 1, St.023
# No. 2, St.033
# No. 3, St.040
# No. 4, St.041
# No. 5, St.045
# No. 7, St.056  
# No. 8, St.078  
# No. 9, St.082 ~ St.083  
# No. 10, St.091 ~ St.092  
sf.loc[(sf['Station No.']=='23'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='33'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='40'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='41'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='45'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='56'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='78'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='82'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='83'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='91'), 'remark'] = 'DIC'
sf.loc[(sf['Station No.']=='92'), 'remark'] = 'DIC'

### CTD DO 채수 정점
# No. 1, St.023
# No. 2, St.034
# No. 3, St.066
# No. 4, St.082
# No. 5, St.084
# No. 6, St.085
# sf.loc[(sf['Station No.']=='23'), 'remark'] = 'DO'
sf.loc[(sf['Station No.']=='23'), 'remark'] = 'DO, DIC'
# sf.loc[(sf['Station No.']=='34'), 'remark'] = 'DO'
# sf.loc[(sf['Station No.']=='66'), 'remark'] = 'DO'
# sf.loc[(sf['Station No.']=='82'), 'remark'] = 'DO'
sf.loc[(sf['Station No.']=='82'), 'remark'] = 'DO, DIC'
sf.loc[(sf['Station No.']=='84'), 'remark'] = 'DO'
sf.loc[(sf['Station No.']=='85'), 'remark'] = 'DO'

# ### Mooring
# # No. 1, WPH
# # No. 2, WPI
# # No. 3, 58I
# # No. 4, 58H
# # No. 5, St.083
# # No. 6, St.092

# sf.loc[(sf['Station No.']=='WPH'), 'remark'] = 'Mooring'
# sf.loc[(sf['Station No.']=='WPI'), 'remark'] = 'Mooring'
# sf.loc[(sf['Station No.']=='58I'), 'remark'] = 'Mooring'
# sf.loc[(sf['Station No.']=='58H'), 'remark'] = 'Mooring'
# sf.loc[(sf['Station No.']=='83'), 'remark'] = 'Mooring'
# sf.loc[(sf['Station No.']=='92'), 'remark'] = 'Mooring'

# ### C-PIES
# # No. 1, St.070
# # No. 2, St.084
# # No. 3, St.085

# # sf.loc[(sf['Station No.']=='70'), 'remark'] = 'C-PIES'
# sf.loc[(sf['Station No.']=='84'), 'remark'] = 'C-PIES, DO'
# sf.loc[(sf['Station No.']=='85'), 'remark'] = 'C-PIES, DO'

# CTD only
sf.loc[(sf.index>=0)&(sf.index<=56)&(sf['No. of Work']==1), 'remark'] = 'CTD Only'
sf.loc[(sf.index>=61)&(sf['No. of Work']<=2), 'remark'] = 'CTD Only'

###
sf.loc[(sf['Station No.']=='34'), 'remark'] = 'CTD Only, DO'
sf.loc[(sf['Station No.']=='45'), 'remark'] = 'CTD Only, DIC'
sf.loc[(sf['Station No.']=='66'), 'remark'] = 'CTD Only, DO'
# sf.loc[(sf['Station No.']=='70'), 'remark'] = 'C-PIES'



px.set_mapbox_access_token(open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read())

 
# fig = px.scatter_mapbox(df, lat="Lat [degree]", lon="Lon [degree]", hover_data=["UTC", "Lat [degree]", "Lon [degree]"],
#                         zoom=0.2, height=375, width=385, center=dict(lat=-30, lon=212))    
fig = px.scatter_mapbox(sf, lat="lat", lon="lon", hover_data=["lat", "lon", "Station No."], color='remark',
                        zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))                                                                       
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.update_traces(marker=dict(size=3), selector=dict(mode='markers'))
fig.update_traces(overwrite=True, marker={"opacity": 0.75, "size": 5})

folder_name='DaDis'
# fname='station_map_do_dic_mooring_c-pies.html'
fname='station_map_ctd_do_dic.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()  


_file='/Users/jung-ok/work1/ARA12B/stationinfo/ARA12B_long_lat_station_20210814.csv'
sf = pd.read_csv(_file)
sf.rename(columns={'Lat_Deg10':'lat', 'Long_Deg10':'lon'}, inplace=True)

sf['remark'] = 'CTD + Other Works'

sf["remark"] = sf["remark"].astype('string') #convert to string
sf['Station No.'] = sf['Station No.'].astype('string')
# sf['Station No.'] = sf['Station No.'].astype(int, errors='ignore')  

# # DIC 채수 정점
# # No. 1, St.023
# # No. 2, St.033
# # No. 3, St.040
# # No. 4, St.041
# # No. 5, St.045
# # No. 7, St.056  
# # No. 8, St.078  
# # No. 9, St.082 ~ St.083  
# # No. 10, St.091 ~ St.092  
# sf.loc[(sf['Station No.']=='23'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='33'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='40'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='41'), 'remark'] = 'DIC'
# # sf.loc[(sf['Station No.']=='45'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='56'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='78'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='82'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='83'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='91'), 'remark'] = 'DIC'
# sf.loc[(sf['Station No.']=='92'), 'remark'] = 'DIC'

# # CTD DO 채수 정점
# # No. 1, St.023
# # No. 2, St.034
# # No. 3, St.066
# # No. 4, St.082
# # No. 5, St.084
# # No. 6, St.085
# # sf.loc[(sf['Station No.']=='23'), 'remark'] = 'DO'
# sf.loc[(sf['Station No.']=='23'), 'remark'] = 'DO, DIC'
# # sf.loc[(sf['Station No.']=='34'), 'remark'] = 'DO'
# # sf.loc[(sf['Station No.']=='66'), 'remark'] = 'DO'
# # sf.loc[(sf['Station No.']=='82'), 'remark'] = 'DO'
# sf.loc[(sf['Station No.']=='82'), 'remark'] = 'DO, DIC'
# # sf.loc[(sf['Station No.']=='84'), 'remark'] = 'DO'
# # sf.loc[(sf['Station No.']=='85'), 'remark'] = 'DO'

### Mooring
# No. 1, WPH
# No. 2, WPI
# No. 3, 58I
# No. 4, 58H
# No. 5, St.083
# No. 6, St.092

sf.loc[(sf['Station No.']=='WPH'), 'remark'] = 'Mooring'
sf.loc[(sf['Station No.']=='WPI'), 'remark'] = 'Mooring'
sf.loc[(sf['Station No.']=='58I'), 'remark'] = 'Mooring'
sf.loc[(sf['Station No.']=='58H'), 'remark'] = 'Mooring'
sf.loc[(sf['Station No.']=='83'), 'remark'] = 'Mooring'
sf.loc[(sf['Station No.']=='92'), 'remark'] = 'Mooring'

### C-PIES
# No. 1, St.070
# No. 2, St.084
# No. 3, St.085
# sf.loc[(sf['Station No.']=='70'), 'remark'] = 'C-PIES'
# sf.loc[(sf['Station No.']=='84'), 'remark'] = 'C-PIES, DO'
# sf.loc[(sf['Station No.']=='85'), 'remark'] = 'C-PIES, DO'
sf.loc[(sf['Station No.']=='84'), 'remark'] = 'C-PIES'
sf.loc[(sf['Station No.']=='85'), 'remark'] = 'C-PIES'

# CTD only
sf.loc[(sf.index>=0)&(sf.index<=56)&(sf['No. of Work']==1), 'remark'] = 'CTD Only'
sf.loc[(sf.index>=61)&(sf['No. of Work']<=2), 'remark'] = 'CTD Only'

###
# sf.loc[(sf['Station No.']=='34'), 'remark'] = 'CTD Only, DO'
# sf.loc[(sf['Station No.']=='45'), 'remark'] = 'CTD Only, DIC'
# sf.loc[(sf['Station No.']=='66'), 'remark'] = 'CTD Only, DO'
sf.loc[(sf['Station No.']=='70'), 'remark'] = 'C-PIES'



px.set_mapbox_access_token(open("/Users/jung-ok/work1/ARA12B/code/.mapbox_token").read())

 
# fig = px.scatter_mapbox(df, lat="Lat [degree]", lon="Lon [degree]", hover_data=["UTC", "Lat [degree]", "Lon [degree]"],
#                         zoom=0.2, height=375, width=385, center=dict(lat=-30, lon=212))    
fig = px.scatter_mapbox(sf, lat="lat", lon="lon", hover_data=["lat", "lon", "Station No."], color='remark',
                        zoom=2, height=350, width=400, center=dict(lat=74, lon=-172.5))                                                                       
# fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.update_traces(marker=dict(size=3), selector=dict(mode='markers'))
fig.update_traces(overwrite=True, marker={"opacity": 0.75, "size": 5})

folder_name='DaDis'
fname='station_map_ctd_mooring_c-pies.html'
_file = '/Users/jung-ok/work1/'+cruise+'/plot/'+folder_name+'/'+fname
fig.write_html(_file)
fig.show()   

 






