#!/bin/bash
cd /Users/jung-ok/work1/geodata/grds

gmt gmtset IO_SEGMENT_MARKER ">"
gmt gmtset FORMAT_GEO_MAP F MAP_FRAME_TYPE plain PS_MEDIA b4
gmt gmtset PS_PAGE_ORIENTATION portrait
gmt gmtset MAP_GRID_PEN_PRIMARY dimgray,...

# Input file, Output file
ps='/Users/jung-ok/work1/ARA12B/figure/map_legend.ps'
png='/Users/jung-ok/work1/ARA12B/figure/map_legend.png'

palette='/Users/jung-ok/work1/geodata/palette/colombia.cpt'
grd='/Users/jung-ok/work1/geodata/grds/ETOPO/ETOPO1_Bed_g_gmt4.grd'
nc='/Users/jung-ok/work1/geodata/grds/ETOPO/etopo1-int.nc'

data='/Users/jung-ok/work1/ARA12B/stationinfo/ARA12B_long_lat_station_20210731.csv'


gmt grdimage $grd -R155/220/64/84 -JS187.5/90/18c -B10f5g5/4f2g2WeSn -I$nc -C$palette -V -K > $ps


gmt pscoast -R155/220/64/84 -JS187.5/90/18c  -B10f5g5/4f2g2WeSn -K -O -Wthinnest,black >> $ps

gmt grdcontour $grd -J -R -A1000+f7p,gray40 -C1000 -L-6000/-1000 -Wthinnest,gray40 -O -K -V >> $ps
# gmt grdcontour $grd -J -R -A500+f8p,gray33 -C500 -L-1000/-500 -Wthinnest,gray17 -O -K -V >> $ps
gmt grdcontour $grd -J -R -A500+f7p,gray40 -C500 -L-1000/-100 -Wthinnest,gray40 -O -K >> $ps
gmt grdcontour $grd -J -R -A50+f7p,gray40 -C50 -L-100/-10 -Wthinnest,gray40 -O -K >> $ps

# # lon lat 
# # -166.542 53.8898 # Dutch Harbor

gmt psxy -R -J  -Ss0.2 -Wdefault,black -Glimegreen -V  -O -K <<EOF>> $ps
-156.788611 71.290556 # Barrow
-165.406389 64.501111 # Nome
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D0.5/0.15 -V -O -K <<EOF>> $ps
-156.788611 71.290556  Barrow
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D0.25/0.16 -V -O -K <<EOF>> $ps
-165.406389 64.501111 Nome
EOF

# ### legend

# ##### CTD Only
# gmt psxy -R -J -Sc0.12 -Gred -Wfaint,black -D-6.3/1. -V -O -K -N <<EOF>> $ps
# 161 82 # 
# EOF

# gmt pstext -F+f8p,Helvetica-Bold=black+jLM  -R -J -D-6./1. -V -O -K -N <<EOF>> $ps
# 161 82  CTD Only
# EOF
# #####

# ##### CTD
# gmt psxy -R -J -Sc0.12 -Gblack -Wfaint,black -D-6.3/.5 -V -O -K -N <<EOF>> $ps
# 161 82 # 
# EOF

# gmt pstext -F+f8p,Helvetica-Bold=black+jLM  -R -J -D-6./.5 -V -O -K -N <<EOF>> $ps
# 161 82  CTD 
# EOF
# #####

# ##### DO
# gmt psxy -R -J -Sc0.20 -Ggreen -Wfaint,black -D-6.3/.0 -V -O -K -N <<EOF>> $ps
# 161 82 # 
# EOF

# gmt pstext -F+f8p,Helvetica-Bold=black+jLM  -R -J -D-6./.0 -V -O -K -N <<EOF>> $ps
# 161 82  DO 
# EOF
# #####

# ##### DIC
# gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black -D-6.3/-0.5 -V -O -K -N <<EOF>> $ps
# 161 82 # 
# EOF

# gmt pstext -F+f8p,Helvetica-Bold=black+jLM  -R -J -D-6./-0.5 -V -O -K -N <<EOF>> $ps
# 161 82  DIC 
# EOF
# #####

gmt pslegend -R -J -O -Dx4.5i/0/1.3i/TR -X-3.0i -Y5.2i -F+p+glightyellow >> $ps << END 
S 0.15i c 0.12 red 0.25p 0.3i CTD Only
S 0.15i c 0.12 black 0.25p 0.3i CTD
S 0.15i c 0.20 green 0.25p 0.3i DO
S 0.15i c 0.28 yellow 0.25p 0.3i DIC
END

gmt psconvert $ps -Au1. -Tg -P
open $png
rm gmt.*