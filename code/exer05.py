import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from matplotlib.ticker import AutoMinorLocator, FixedLocator, MultipleLocator
import pandas as pd

def map_common(ax1,gl_loc=[True,True,False,True],gl_lon_info=range(-180,180,60),gl_dlat=30):

    # ax1.coastlines(color='silver',linewidth=1.)
    ax1.coastlines(resolution='10m', color='darkgray',linewidth=1.)
    ax1.stock_img()

    gl = ax1.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                       linewidth=0.6, color='gray', alpha=0.5, linestyle='--')

    gl.ylabels_left = gl_loc[0]
    gl.ylabels_right = gl_loc[1]
    gl.xlabels_top = gl_loc[2]
    gl.xlabels_bottom = gl_loc[3]

    gl.xlocator = FixedLocator(gl_lon_info)
    gl.ylocator = MultipleLocator(gl_dlat)
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 11, 'color': 'k'}
    gl.ylabel_style = {'size': 11, 'color': 'k'}

    
gps_data=pd.read_csv('/Users/jung-ok/work1/ANA11/processed/DaDiS/GPS_1min.csv', index_col=[0], parse_dates=True)   


# latdata=gps_data['Latitude']
# londata=gps_data['Longitude']




# lon_boundary=np.arange(-240,-60,1.)
# lat_boundary=np.arange(15,75,1.)
# data=np.ones([lat_boundary.shape[0]-1,lon_boundary.shape[0]-1]) ## Data dimension is 1 less than boundaries
# data=data*lat_boundary[:-1,None]

lon_offset=-135  ##
latdata=gps_data['Latitude']
londata=gps_data['Longitude']


fig=plt.figure()
# fig.set_size_inches(7.5,5) ## (xsize, ysize)
fig.set_size_inches(10,8) ## (xsize, ysize)
ax1=fig.add_subplot(111,projection=ccrs.PlateCarree(central_longitude=lon_offset))
ax1.set_extent([-250,-20,-80,50],crs=ccrs.PlateCarree())
# ax1.plot(lon2d, lat2d, ls='-', c='orange')

plt.plot(londata, latdata, ls='', marker='o', ms=0.5, c='orange', transform=ccrs.PlateCarree())



# ax1.set_title('Lon_Offset=-90')
# map_common(ax1,gl_lon_info=[-180,-120,-60,120,],gl_dlat=15)
# map_common(ax1,gl_lon_info=[-180,-120,-50,-60, 110, 120,],gl_dlat=15)
map_common(ax1,gl_lon_info=[-180,-120, -60, 120,],gl_dlat=30)




fnout='./exer05.png'
plt.savefig(fnout,bbox_inches='tight',dpi=150)
plt.show()
