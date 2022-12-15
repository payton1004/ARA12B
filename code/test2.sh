#!/bin/bash
cd /Users/jung-ok/work1/ARA12B/figure/sic/daily/

gmt set IO_SEGMENT_MARKER ">"
gmt set FORMAT_GEO_MAP F
gmt set MAP_FRAME_TYPE plain
gmt set PS_MEDIA a4

gmt set FONT_LABEL black
gmt set MAP_FRAME_PEN thicker,black
gmt set FONT_ANNOT_PRIMARY black
gmt set FONT_ANNOT_SECONDARY black
gmt set MAP_TICK_PEN_PRIMARY black
gmt set MAP_TICK_PEN_SECONDARY black

#
gmt gmtset MAP_GRID_PEN_PRIMARY dimgray,...
#


palette=/Users/jung-ok/work1/geodata/palette/land.cpt
grd=/Users/jung-ok/work1/geodata/grds/IBCAO/IBCAO_V3_30arcsec_RR.grd
nc=/Users/jung-ok/work1/geodata/grds/ibcao-int.nc

track=/Users/jung-ok/work1/ARA12B/processed/DaDiS/LonLat_6hour_intervals.csv

data='/Users/jung-ok/work1/ARA12B/stationinfo/ARA12B_long_lat_station_20210814.csv'

# araon='/Users/jung-ok/work1/symbol_logo/processed/ibrv-araon.png'

sic=/Users/jung-ok/work1/amsr2data/n3125/2021/jul/asi-AMSR2-n3125-20210721-v5.csv

date=20210721
year=2021
month=07
day=21

# 2021-07-21 00:00:00,191.613,65.6302,0
lon=-168.3872
lat=65.6302

val=0


#path=/Users/jung-ok/work1/ARA12B/figure/sic/daily/
h=$date'00h'


### 00:00:00
# ps=$h.ps
# png=$h.png

ps=test2.ps
png=test2.png


gmt grdimage $grd -R155/220/64/84 -JS187.5/90/18c  -B10f5g5/4f2g2WeSn  -I$ncfile -C$palette -V -K > $ps
gmt pscoast -R155/220/64/84 -JS187.5/90/18c  -B10f5g5/4f2g2WeSn -K -O -Wthinnest,black >> $ps

# Sea ice
gmt makecpt -Cabyss -T0/100/2 > ice.cpt
awk -F, '{if (NR>1 && $3!=nan) print $1, $2, $3}' $sic | gmt psxy -R -JS -Cice.cpt -Ss0.08 -O -K >> $ps

#color bar
gmt psscale  -D3.55i/-0.5i/2.7i/0.15ih -Cice.cpt -B20f5:"sea ice (%)": -O -V -K  >> $ps

#ARA12B
#track
awk -F, '{if (NR>1) print $1, $2}' $data  | gmt psxy -R -J -Wthick,orange -O -V -K >> $ps

### 정점 표시 Station 1 ~ 92

# CTD
awk -F, '{if (NR>1 && $4>2) print $1, $2}' $data | \
	gmt psxy -JS -R -Sc0.12 -Ggray0 -Wfaint,gray  -O -V -K >> $ps

# CTD only
awk -F, '{if (NR>1 && NR<=58 && $4<=2) print $1, $2}' $data | \
	gmt psxy -JS -R -Sc0.12 -Gred -Wfaint,black  -O -V -K >> $ps    

awk -F, '{if (NR>=63 && $4<=2) print $1, $2}' $data | \
	gmt psxy -JS -R -Sc0.12 -Gred -Wfaint,black  -O -V -K >> $ps  

# Station numbers
# 1 ~ 4
awk -F, '{if (NR>1 && NR<=5) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,gray+jCM  -V  -O -K -D0.10/0.06  >> $ps

# 5 ~ 10
awk -F, '{if (NR>5 && NR<=11) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,gray+jCM  -V  -O -K -D-0.09/0.06  >> $ps

# 11 ~ 17
awk -F, '{if (NR>11 && NR<=18) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,gray+jCM  -V  -O -K -D0.12/0.06  >> $ps

# 18 ~ 19
awk -F, '{if (NR>18 && NR<=20) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.12/0.06  >> $ps

# 20 ~ 33
awk -F, '{if (NR>20 && NR<=34) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/0.06  >> $ps

# 34 ~ 39
awk -F, '{if (NR>34 && NR<=40) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/0.06  >> $ps

# 40
awk -F, '{if (NR==41) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 41
awk -F, '{if (NR==42) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 42 ~ 51
awk -F, '{if (NR>42 && NR<=52) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/0.06  >> $ps

# 52 ~ 56
awk -F, '{if (NR>52 && NR<=57) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 57
awk -F, '{if (NR==58) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/-0.06  >> $ps

#WPH
awk -F, '{if (NR==59) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM -V  -O -K -D-0.06/-0.08  >> $ps

# WPI
awk -F, '{if (NR==60) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM -V  -O -K -D-0.18/0.1  >> $ps

# 58I
awk -F, '{if (NR==61) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM   -V  -O -K -D0.05/0.1  >> $ps

# 58H
awk -F, '{if (NR==62) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM   -V  -O -K -D0.14/-0.01  >> $ps

# 59 ~ 60
awk -F, '{if (NR>62 && NR<=64) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.13/0.06  >> $ps

# 61 ~ 62
awk -F, '{if (NR>64 && NR<=66) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.0/0.13  >> $ps

# 63 ~ 65
awk -F, '{if (NR>66 && NR<=69) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0./-0.13  >> $ps

# 66 ~ 68
awk -F, '{if (NR>69 && NR<=72) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0./-0.13  >> $ps

# 69
awk -F, '{if (NR==73) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.15/-0.  >> $ps

# 70
awk -F, '{if (NR==74) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.15/-0.  >> $ps

# 71
awk -F, '{if (NR==75) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0./0.13  >> $ps

# 72
awk -F, '{if (NR==76) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.15/-0.  >> $ps

# 73 ~ 80
awk -F, '{if (NR>76 && NR<=84) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/-0.06  >> $ps

# 81 ~ 85
awk -F, '{if (NR>84 && NR<=89) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/-0.06  >> $ps

# 86 ~ 88
awk -F, '{if (NR>89 && NR<=92) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0./-0.12  >> $ps

# 89 ~ 90
awk -F, '{if (NR>92 && NR<=94) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0./-0.12  >> $ps


# 91 ~ 92
awk -F, '{if (NR>94 && NR<=96) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/-0.06  >> $ps


### position of ship

# gmt psxy -J -R -Sc0.15 -G0/205/0 -Wthinner,red -O -V -K <<EOF>> $ps
# $lon $lat
# EOF

gmt psxy -J -R -Sc0.25 -G0/205/0 -Wthick,#1a9850 -O -V -K <<EOF>> $ps
$lon $lat
EOF

# gmt psxy -J -R -Sx0.20 -Wthick,0/205/0 -O -V -K <<EOF>> $ps
# $lon $lat
# EOF



# gmt psimage -R -J -V -K -O -C10.6/14.4 -D0.3/3.5 $araon -W1.1i >> $ps


gmt psxy -R -J  -Sc0.2 -Wdefault,black -Gwhite -V  -O -K <<EOF>> $ps
-156.788611 71.290556 # Barrow
-165.406389 64.501111 # Nome
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0.35/-0.3 -V -O -K <<EOF>> $ps
-156.788611 71.290556  Barrow
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0.25/0.25 -V -O -K  <<EOF>> $ps
-165.406389 64.501111 Nome
EOF


gmt pstext -J -R -F+f14p,Helvetica-Bold=thickest,white -D.7/.7 -V -O -K  <<EOF>> $ps
$lon $lat $val (%)
EOF

gmt pstext -J -R -F+f14p,Helvetica,black -D.7/.7 -V -O -K  <<EOF>> $ps
$lon $lat $val (%)
EOF

# gmt pstext -J -R -F+f14p,Helvetica,black -Gwhite -O -V -Y2.0 -K  <<EOF>> $ps
# -172.5 83 $val (%)
# EOF

gmt pstext -J -R -F+f16p,Helvetica,black  -O -V -Y2.5  <<EOF>> $ps
-172.5 83 $year-$month-$day 00h
EOF
# gmt pstext -J -R -F+f16p,Helvetica,black -Gwhite -O -V -Y0.8  <<EOF>> $ps
# -172.5 83 $year-$month-$day 00h
# EOF

# gmt ps2raster $ps -Au1.5 -Tf -P
gmt psconvert $ps -Au1.5 -Tg -P

open $png
rm gmt.*
