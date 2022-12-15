#!/bin/bash
cd /Users/jung-ok/work1/geodata/grds

gmt gmtset IO_SEGMENT_MARKER ">"
gmt gmtset FORMAT_GEO_MAP F MAP_FRAME_TYPE plain PS_MEDIA b4
gmt gmtset PS_PAGE_ORIENTATION portrait
gmt gmtset MAP_GRID_PEN_PRIMARY dimgray,...


grd='/Users/jung-ok/work1/geodata/grds/ETOPO/ETOPO1_Bed_g_gmt4.grd'
nc='/Users/jung-ok/work1/geodata/grds/ETOPO/etopo1-int.nc'
palette=/Users/jung-ok/work1/geodata/palette/colombia.cpt
track=/Users/jung-ok/work1/ARA12B/processed/DaDis/GPS/GPS_1min.csv

# eez01='/Users/jung-ok/work1/geodata/eez/Alaska_EEZ_line.txt'
# eez02='/Users/jung-ok/work1/geodata/eez/Canada_EEZ_line.txt'
# eez03='/Users/jung-ok/work1/geodata/eez/Russia_EEZ_line.txt'

ps=/Users/jung-ok/work1/ARA12B/figure/spatial/track_ARA12.ps
jpg=/Users/jung-ok/work1/ARA12B/figure/spatial/track_ARA12.jpg


region=120/250/17/81
proj=M185/49/17
# proj=m0.08


# gmt grdimage $grd -R120/220/30/80 -JM170/55/15 -B20f5g5/10f5g5WeSn -I$nc -C$palette -V -K > $ps
gmt grdimage $grd -R$region -J$proj -B20f5g5/10f5g5WeSn -I$nc -C$palette -V -K > $ps
gmt pscoast -R -J  -B -K -O  -Wthinnest,black >> $ps

# gmt grdcontour $grd -J -R -A1000+f7p,gray40 -C1000 -L-3000/-1000 -Wthinnest,gray40 -O -K -V >> $ps
# # gmt grdcontour $grd -J -R -A500+f8p,gray33 -C500 -L-1000/-500 -Wthinnest,gray17 -O -K -V >> $ps
# gmt grdcontour $grd -J -R -A500+f7p,gray40 -C500 -L-1000/-100 -Wthinnest,gray40 -O -K >> $ps
# gmt grdcontour $grd -J -R -A50+f7p,gray40 -C50 -L-100/-10 -Wthinnest,gray40 -O -K >> $ps


# #EEZ Alaska
# awk -F, '{print $1, $2}' $eez01  | gmt psxy -R -J -Wdefault,white,--  -O -V -K  >> $ps
# #EEZ Canada
# awk -F, '{print $1, $2}' $eez02  | gmt psxy -R -J -Wdefault,white,--  -O -V -K  >> $ps
# #EEZ Russia
# awk -F, '{print $1, $2}' $eez03  | gmt psxy -R -J -Wdefault,white,--  -O -V -K  >> $ps

# Pacific Ocean
gmt pstext -F+f10.p,Helvetica-BoldOblique,gray  -R -J -D0/5. -N -V -O -K <<EOF>> $ps
-160 0  PACIFIC OCEAN 
EOF

# Sea of Okhotsk
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0./0.1 -V -O -K <<EOF>> $ps
150 55  OKHOTSK
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0./0.1 -V -O -K <<EOF>> $ps
150 55  OKHOTSK
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0./-0.2 -V -O -K <<EOF>> $ps
150 55   SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0./-0.2 -V -O -K <<EOF>> $ps
150 55   SEA
EOF

# Bering SEA
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0.3/0.1 -V -O -K <<EOF>> $ps
-178 58  BERING
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0.3/0.1 -V -O -K <<EOF>> $ps
-178 58  BERING
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0.3/-0.2 -V -O -K <<EOF>> $ps
-178 58  SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0.3/-0.2 -V -O -K <<EOF>> $ps
-178 58  SEA
EOF

# Chukchi SEA
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0.3/0.1 -V -O -K <<EOF>> $ps
-172 69  CHUKCHI
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0.3/0.1 -V -O -K <<EOF>> $ps
-172 69  CHUKCHI
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0.3/-0.2 -V -O -K <<EOF>> $ps
-172 69  SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0.3/-0.2 -V -O -K <<EOF>> $ps
-172 69  SEA
EOF

# Beaufort SEA (137W, 72N)
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0/0.1 -V -O -K <<EOF>> $ps
-137 72  BEAUFORT
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0/0.1 -V -O -K <<EOF>> $ps
-137 72  BEAUFORT
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0/-0.2 -V -O -K <<EOF>> $ps
-137 72  SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0/-0.2 -V -O -K <<EOF>> $ps
-137 72  SEA
EOF

# Laptev SEA (125E, 76N)
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0/0.1 -V -O -K <<EOF>> $ps
125.633 76.266  LAPTEV
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0/0.1 -V -O -K <<EOF>> $ps
125.633 76.266 LAPTEV
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0/-0.2 -V -O -K <<EOF>> $ps
125.633 76.266  SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0/-0.2 -V -O -K <<EOF>> $ps
125.633 76.266  SEA
EOF

# East siberian SEA (163E, 72N)
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D0.0/0.1 -V -O -K <<EOF>> $ps
163 72  EAST
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D0.0/0.1 -V -O -K <<EOF>> $ps
163 72   EAST
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D0.0/-0.2 -V -O -K <<EOF>> $ps
163 72   SIBERIAN
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D0.0/-0.2 -V -O -K <<EOF>> $ps
163 72   SIBERIAN
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D0.0/-0.5 -V -O -K <<EOF>> $ps
163 72  SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D0.0/-0.5 -V -O -K <<EOF>> $ps
163 72   SEA
EOF

# Wrangelya Island
gmt pstext -F+f6p,Helvetica-Bold,black  -R -J -D0./0. -V -O -K <<EOF>> $ps
-179.41667 71.2333333 Wrangelya I.
EOF

# New Siberian Islands
gmt pstext -F+f6p,Helvetica-Bold,black  -R -J -D0./0. -V -O -K <<EOF>> $ps
145.25 75.266 New Siberian I.
EOF

# Aleutian Islands
gmt pstext -F+f6p,Helvetica-Bold=thickest,white  -R -J -D0./-0.3 -V -O -K <<EOF>> $ps
-174.2 52.2 Aleutian I.
EOF

gmt pstext -F+f6p,Helvetica-Bold,black  -R -J -D0./-0.3 -V -O -K <<EOF>> $ps
-174.2 52.2 Aleutian I.
EOF

# # USA
# gmt pstext -F+f8p,Helvetica-Bold,black  -R -J -D-7./6. -N -V -O -K <<EOF>> $ps
# -100 40 USA
# EOF

# Alaska
gmt pstext -F+f7p,Helvetica-Bold,black  -R -J -D-0./0.5 -N -V -O -K <<EOF>> $ps
-152.2782 64.0685 ALASKA
EOF

# Canada
gmt pstext -F+f8p,Helvetica-Bold,black  -R -J -D-2./1. -N -V -O -K <<EOF>> $ps
-110 60 CANADA
EOF

# Russia
gmt pstext -F+f8p,Helvetica-Bold,black  -R -J -D7./2. -N -V -O -K <<EOF>> $ps
90 60 RUSSIA
EOF



# Bering Strait
gmt pstext -F+a88+f6p,Helvetica-Oblique,blue  -R -J -D-0./0.1 -V -O -K <<EOF>> $ps
-169.82833333 65.09111111  Bering Strait
EOF

# Brooks Range
gmt pstext -F+a24+f6.2p,Helvetica-Oblique,black  -R -J -D0./0. -V -O -K <<EOF>> $ps
-152.25 68.2  BROOKS RANGE
EOF

# Canada Basin
gmt pstext -F+a0+f7p,Helvetica-Bold=thickest,white  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
-143.27153 77.353563  CANADA BASIN
EOF
gmt pstext -F+a0+f7p,Helvetica-Bold,blue  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
-143.27153 77.353563  CANADA BASIN
EOF

# # Canada Abyssal Plain
# gmt pstext -F+a289+f6.5p,Helvetica-Bold,gray  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
# -150 78  CANADA ABYSSAL PLAIN
# EOF

# Northwind Ridge
gmt pstext -F+a267+f5p,Helvetica-oblique,gray  -R -J -D0.15/-0 -V -O -K <<EOF>> $ps
-157.10482 76.718071  NORTHWIND RIDGE
EOF

# Northwind ABYSSAL PLAIN
gmt pstext -F+a259+f5p,Helvetica-oblique,gray  -R -J -D-0.25/-0 -V -O -K <<EOF>> $ps
-157.2363476 77.51653299  NORTHWIND ABYSSAL PLAIN
EOF

# Chukchi Plateau
gmt pstext -F+a0+f5p,Helvetica,gray23  -R -J -D-0.1/0.9 -V -O -K <<EOF>> $ps
-166 77  CHUKCHI 
EOF
gmt pstext -F+a0+f5p,Helvetica,gray23  -R -J -D-0.1/0.7 -V -O -K <<EOF>> $ps
-166 77  PLATEAU
EOF

# Chukchi ABYSSAL PLAIN
gmt pstext -F+a0+f5p,Helvetica,gray  -R -J -D-0.2/0.25 -V -O -K <<EOF>> $ps
-172 76.75  CHUKCHI 
EOF
gmt pstext -F+a0+f5p,Helvetica,gray  -R -J -D-0.2/-0.05 -V -O -K <<EOF>> $ps
-172 76.75  ABYSSAL PLAIN
EOF

# Mendeleev ABYSSAL PLAIN
gmt pstext -F+a340+f5p,Helvetica,gray  -R -J -D0./0. -V -O -K <<EOF>> $ps
-169 81.5  MENDELEEV 
EOF
gmt pstext -F+a340+f5p,Helvetica,gray  -R -J -D0./-0.3 -V -O -K <<EOF>> $ps
-169 81.5  ABYSSAL PLAIN
EOF

# Mendeleev RIDGE
gmt pstext -F+a92+f6p,Helvetica-Bold=thickest,white  -R -J -D-0/-0.3 -V -O -K <<EOF>> $ps
-178 80  MENDELEEV  RIDGE
EOF
gmt pstext -F+a92+f6p,Helvetica-Bold,blue  -R -J -D-0/-0.3 -V -O -K <<EOF>> $ps
-178 80  MENDELEEV  RIDGE
EOF

#Kucherov Terrace
gmt pstext -F+a300+f5p,Helvetica,gray  -R -J -D0.3/0. -V -O -K <<EOF>> $ps
174.53196401 77.7192987   KUCHEROV
EOF
gmt pstext -F+a300+f5p,Helvetica,gray  -R -J -D-0.0/-0. -V -O -K <<EOF>> $ps
174.53196401 77.7192987   TERRACE
EOF
# gmt pstext -F+a39+f6.2p,Helvetica,blue  -R -J -D0./-0 -V -O -K <<EOF>> $ps
# 174.53196401 77.7192987  KUCHEROV TERRACE
# EOF

# Wrangel ABYSSAL PLAIN
gmt pstext -F+a30+f5p,Helvetica,gray  -R -J -D-0.15/0.05 -V -O -K <<EOF>> $ps
170 82.5  WRANGEL 
EOF
gmt pstext -F+a30+f5p,Helvetica,gray  -R -J -D-0.15/-0.25 -V -O -K <<EOF>> $ps
170 82.5  ABYSSAL PLAIN
EOF

# Makarov Basin (140E, 88N)
gmt pstext -F+a0+f7p,Helvetica-Bold=thickest,white  -R -J -D2.5/-11.5 -N -V -O -K <<EOF>> $ps
140 88  MAKAROV BASIN
EOF
gmt pstext -F+a0+f7p,Helvetica-Bold,blue  -R -J -D2.5/-11.5 -N -V -O -K <<EOF>> $ps
140 88  MAKAROV BASIN
EOF

# Amundsen Basin (99.81963169E, 86.25701641N)
gmt pstext -F+a0+f7p,Helvetica-Bold=thickest,white  -R -J -D4.0/-7.0 -N -V -O -K <<EOF>> $ps
99.81963169 86.25701641  AMUNDSEN BASIN
EOF
gmt pstext -F+a0+f7p,Helvetica-Bold,blue  -R -J -D4.0/-7.0 -N -V -O -K <<EOF>> $ps
99.81963169 86.25701641  AMUNDSEN BASIN
EOF



#ARA12
#track
awk -F, '{if (NR>1) print $3, $2}' $track  | gmt psxy -R -J -Wthick,orange -O -V -K  >> $ps


gmt psxy -R -J  -Sc0.2 -W0.25p -Gred -V  -O -K <<EOF>> $ps
# -165.406389 64.501111 # Nome
# -156.788611 71.290556 # Barrow
127.681201 34.915621 # Gwangyang
-166.516 53.9 # Dutch Harbor
EOF



gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D0.5/-0.25 -N -V  -O -K <<EOF>> $ps
-166.516 53.9  Dutch Harbor
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0.5/-0.25 -N -V  -O -K <<EOF>> $ps
-166.516 53.9  Dutch Harbor
EOF


gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D0.2/0.2 -N -V  -O -K <<EOF>> $ps
-122.316 47.6  Seattle
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0.2/0.2 -N -V  -O -K <<EOF>> $ps
-122.316 47.6  Seattle
EOF

gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D-0.2/-0.2 -N -V  -O -K <<EOF>> $ps
-122.45 47.233  Tacoma
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D-0.2/-0.2 -N -V  -O -K <<EOF>> $ps
-122.45 47.233  Tacoma
EOF



gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D0./0. -N -V  -O -K <<EOF>> $ps
-147.716 64.833  Fairbanks
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0./0. -N -V  -O -K <<EOF>> $ps
-147.716 64.833  Fairbanks
EOF

gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D0./0. -N -V  -O -K <<EOF>> $ps
-149.9 61.216  Anchorage
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0./0. -N -V  -O -K <<EOF>> $ps
-149.9 61.216  Anchorage
EOF

gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D0.25/0.2 -N -V  -O -K <<EOF>> $ps
-157.85 21.3  Honolulu
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0.25/0.2 -N -V  -O -K <<EOF>> $ps
-157.85 21.3  Honolulu
EOF


# gmt pstext -R -J  -F+f7p,Helvetica-Bold,black+jCM -Gyellow -D0.5/0.25 -V  -O -K <<EOF>> $ps
gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D0./0. -N -V  -O -K <<EOF>> $ps
-165.406389 64.501111  Nome
-156.788611 71.290556  Barrow
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0./0. -N -V  -O -K <<EOF>> $ps
-165.406389 64.501111  Nome
-156.788611 71.290556  Barrow
EOF


# gmt pstext -R -J  -F+f7p,Helvetica-Bold,black+jCM -Gyellow -D-0.4/0.35 -V  -O  <<EOF>> $ps
gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D0.4/-0.35 -N -V  -O -K <<EOF>> $ps
127.681201 34.915621   Gwangyang
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D0.4/-0.35 -N -V  -O -K <<EOF>> $ps
127.681201 34.915621   Gwangyang
EOF

gmt pstext -R -J  -F+f7p,Helvetica=thickest,white  -D-0./0. -N -V  -O -K <<EOF>> $ps
126.633 37.483   Incheon
EOF

gmt pstext -R -J  -F+f7p,Helvetica,gray23  -D-0./0. -N -V  -O -K <<EOF>> $ps
126.633 37.483   Incheon
EOF

### Main Schedule
gmt psxy -R -J  -Sc0.1  -Gyellow -W0.15p   -V  -O -K <<EOF>> $ps
127.681201 34.915621 
165.9403   50.2015
-174.9042   56.3155
-168.4342   64.9848
-171.6294   75.1993
-165.0932   72.5642
-171.1659   58.5859
127.681201 34.915621 
EOF

gmt pstext -R -J  -F+f6p,Helvetica=thick,gray87  -D-0.2/0.18 -N -V -O -K <<EOF>> $ps
127.681201 34.915621 07-01 
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D-0.2/0.18 -N -V -O -K <<EOF>> $ps
127.681201 34.915621 07-01 
EOF

gmt pstext -R -J  -F+f6p,Helvetica=thick,gray87  -D0.2/0.18 -N -V  -O -K <<EOF>> $ps
-168.4342   64.9848 07-20
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D0.2/0.18 -N -V -O -K <<EOF>> $ps
-168.4342   64.9848 07-20
EOF

gmt pstext -R -J  -F+f6p,Helvetica=thick,gray87  -D0./-0.2 -N -V -O -K <<EOF>> $ps
# 127.681201 34.915621 07-01 
165.9403   50.2015 07-08 
-174.9042   56.3155 07-14 
# -168.4342   64.9848 07-20
-171.6294   75.1993 08-18 
-165.0932   72.5642 09-09 
-171.1659   58.5859 09-12 
# 127.681201 34.915621 09-23 
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D0./-0.2 -N -V  -O -K  <<EOF>> $ps
# 127.681201 34.915621 07-01 
165.9403   50.2015 07-08 
-174.9042   56.3155 07-14 
# -168.4342   64.9848 07-20
-171.6294   75.1993 08-18 
-165.0932   72.5642 09-09 
-171.1659   58.5859 09-12 
# 127.681201 34.915621 09-23 
EOF


gmt pstext -R -J  -F+f6p,Helvetica=thick,gray87  -D0.2/-0.18 -N -V -O -K <<EOF>> $ps
127.681201 34.915621 09-23 
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D0.2/-0.18 -N -V -O  <<EOF>> $ps
127.681201 34.915621 09-23 
EOF


gmt psconvert -Au -Tj $ps

open $jpg