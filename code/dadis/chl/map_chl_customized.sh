#!/bin/bash
# cd /Users/jung-ok/work1/geodata/grds
gmt set FONT_LABEL black
gmt set MAP_FRAME_PEN thicker,black
gmt set FONT_ANNOT_PRIMARY black
gmt set FONT_ANNOT_SECONDARY black
gmt set MAP_TICK_PEN_PRIMARY black
gmt set MAP_TICK_PEN_SECONDARY black
gmt gmtset IO_SEGMENT_MARKER ">"
gmt gmtset PS_MEDIA a4
# gmt gmtset FORMAT_GEO_MAP F MAP_FRAME_TYPE plain PS_MEDIA a4
gmt gmtset FORMAT_GEO_MAP F 
gmt gmtset MAP_GRID_PEN_PRIMARY dimgray,...
gmt gmtset MAP_FRAME_TYPE fancy
gmt gmtset MAP_FRAME_WIDTH  5p


track=/Users/jung-ok/work1/ARA12B/processed/DaDis/GPS/GPS_1min_ara12b.csv
# sic=/Users/jung-ok/work1/ARA12B/processed/track_sic/track_sic_all_n3125.csv
infile=/Users/jung-ok/work1/ARA12B/processed/DaDis/Fluorometer/chl/utc_lon_lat_chl_10min_mean.csv

ps=/Users/jung-Ok/work1/ARA12B/figure/spatial/ARA12B_Chl_cb_10_RdYlBu.ps
png=/Users/jung-Ok/work1/ARA12B/figure/spatial/ARA12B_Chl_cb_10_RdYlBu.png

palette=/Users/jung-ok/work1/geodata/palette/colombia.cpt
palette2=/Users/jung-ok/work1/ARA12B/code/dadis/chl/chl_ara12b.cpt


x_offset=0.25
y_offset=0.15
region=155/220/64/84
proj=S187.5/90/18c

# gmt grdimage $grd -R155/220/64/84 -JS187.5/90/18c -B10f5g5/4f2g2WeSn -I$nc -C$palette -V -K > $ps
# gmt pscoast -R155/220/64/84 -JS187.5/90/18c  -B10f5g5/4f2g2WeSn -K -O -Wthinnest,black >> $ps

gmt psbasemap  -R$region -J$proj -X$x_offset -Y$y_offset -Ba10f5g5/a4f2g2WeSn  -V -K > $ps
gmt pscoast -R -J -B  -K -Ggray -O >> $ps

# Coast
awk -F, '{print $1, $2}' /Users/jung-ok/work1/geodata/textfile/coastlines.txt | \
gmt psxy -R -JS -W -Ggray  -K -O >> $ps

# grounding
awk -F, '{print $1, $2}' /Users/jung-ok/work1/geodata/textfile/grounding.txt | \
gmt psxy -JS -R -Ggray -W -L -O -K >> $ps

# islands
awk '{if (NR>1) print $1, $2}' /Users/jung-ok/work1/geodata/textfile/islands_all.txt | \
gmt psxy -JS -R -Ggray -W -O -K  >> $ps


# 
# gmt makecpt -Cno_green -T0/100/2 > color.cpt
# awk -F, '{if (NR>1 && $2>=65.1735) print $1, $2, $3}' $sic | gmt psxy -R -J -Ccolor.cpt -Sc0.25 -O -K >> $ps
# vertical color bar
# gmt makecpt -Cno_green -T3.0/27.0/0.1 > color.cpt
# awk -F, '{print $2,$3,$4}' $infile |  gmt psxy -JS -R -Ccolor.cpt -Sc0.2 -O -K -V  >> $ps
awk -F, '{print $2,$3,$4}' $infile |  gmt psxy -JS -R -C$palette2 -Sc0.2 -O -K -V  >> $ps
 


# color bar
# gmt psscale  -D7.5i/2.8i/5.8i/0.17i -Ccolor.cpt -B20f5:"sea ice concentration(%)": -O -V -K  >> $ps
# gmt psscale -Ebf -D7.5i/2.8i/5.8i/0.17i -Ccolor.cpt -B3.0f1.0:"Chlorophyll-a (\265g/L)": -O -K >> $ps
gmt psscale -Ebf -D7.5i/2.8i/5.8i/0.17i -C$palette2 -L -O -K >> $ps
# gmt psscale -Ebf -D7.5i/2.8i/5.8i/0.17i -C$palette2 -B3.0:"Chlorophyll-a (\265g/L)": -O -K >> $ps

#ARA12B
#track
awk -F, '{if (NR>1) print $2, $3}' $track  | gmt psxy -R -J -Wthinner,black -O -V -K >> $ps
# awk -F, '{if (NR>1 && $2>=65.1735) print $1, $2}' $sic  | gmt psxy -R -J -Wthick,orange -O -V -K >> $ps


gmt pstext -R -J  -F+f18p,Helvetica-Bold,Black  -D0.12/0.17 -V -O -K <<EOF>> $ps
170 66  Russia
EOF

gmt pstext -R -J  -F+f18p,Helvetica-Bold,Black  -D0.1/0.19 -V -O -K  <<EOF>> $ps
208 66 Alaska
EOF


gmt psxy -R -J  -Ss0.4 -Wdefault,black -Glightsteelblue -V  -O -K <<EOF>> $ps
-156.788611 71.290556 # Barrow
-165.406389 64.501111 # Nome
EOF

gmt pstext -R -J  -F+f12p,Helvetica-Bold,Black  -D0.3/-0.5 -V -O -K <<EOF>> $ps
-156.788611 71.290556  Barrow
EOF

gmt pstext -R -J  -F+f12p,Helvetica-Bold,Black  -D0.3/0.5 -V -O -K <<EOF>> $ps
-165.406389 64.501111 Nome
EOF

gmt pstext -J -R -F+a90+f14p,black+jCM -X9.5 -Y1.9  -N -O  <<EOF>> $ps
-156.788611 71.290556 Chlorophyll-a (\265g/L)
EOF

gmt psconvert $ps -Au1.5 -Tg 

open $png
rm gmt.*