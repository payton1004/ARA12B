#!/bin/bash
cd /Users/jung-ok/work1/geodata/grds

##
gmt gmtset IO_SEGMENT_MARKER ">"
gmt gmtset FORMAT_GEO_MAP F MAP_FRAME_TYPE plain PS_MEDIA b4

# gmt gmtset PS_PAGE_ORIENTATION landscape
gmt gmtset PS_PAGE_ORIENTATION portrait

# gmt gmtset COLOR_FOREGROUND blue

# gmt gmtset FONT_ANNOT_PRIMARY 12p
# gmt gmtset PROJ_SCALE_FACTOR 0.97276926983
# gmt gmtset MAP_GRID_PEN_PRIMARY black
# gmt gmtset MAP_GRID_PEN_SECONDARY black
gmt gmtset MAP_GRID_PEN_PRIMARY dimgray,...
# gmt gmtset MAP_POLAR_CAP None
# gmt gmtset MAP_POLAR_CAP 89/90

# echo "no error"

# Input file, Output file
ps=/Users/jung-ok/work1/ARA12B/figure/ARA12B_station_1_98.ps
png=/Users/jung-ok/work1/ARA12B/figure/ARA12B_station_1_98.png

palette=/Users/jung-ok/work1/geodata/palette/colombia.cpt
grd=/Users/jung-ok/work1/geodata/grds/ETOPO/ETOPO1_Bed_g_gmt4.grd
nc=/Users/jung-ok/work1/geodata/grds/ETOPO/etopo1-int.nc

data='/Users/jung-ok/work1/ARA12B/stationinfo/ARA12B_station_lat_long_20210727.csv'

eez01='/Users/jung-ok/work1/geodata/eez/Alaska_EEZ_line.txt'
eez02='/Users/jung-ok/work1/geodata/eez/Canada_EEZ_line.txt'
eez03='/Users/jung-ok/work1/geodata/eez/Russia_EEZ_line.txt'

araon='/Users/jung-ok/work1/symbol_logo/processed/ibrv-araon.png'
kopri='/Users/jung-ok/work1/symbol_logo/processed/kopri_ci_eng_height.gif'
bear='/Users/jung-ok/work1/symbol_logo/other/bear01.png'

gmt grdimage $grd -R155/220/64/84 -JS187.5/90/18c -B10f5g5/4f2g2WeSn -I$nc -C$palette -V -K > $ps

gmt psimage -R -J -V -K -O -C10.6/14.4 -D0.3/3.5 $araon -W1.1i >> $ps
gmt psimage -R -J -V -K -O -C7.55/14.4 -D0.3/3.5 $kopri -W1.1i  >> $ps
gmt psimage -R -J -V -K -O -C5.3/14.4 -D0.3/3.5 $bear -W0.7i  >> $ps

gmt pscoast -R155/220/64/84 -JS187.5/90/18c  -B10f5g5/4f2g2WeSn -K -O -Wthinnest,black >> $ps

gmt grdcontour $grd -J -R -A1000+f7p,gray40 -C1000 -L-6000/-1000 -Wthinnest,gray40 -O -K -V >> $ps
# gmt grdcontour $grd -J -R -A500+f8p,gray33 -C500 -L-1000/-500 -Wthinnest,gray17 -O -K -V >> $ps
gmt grdcontour $grd -J -R -A500+f7p,gray40 -C500 -L-1000/-100 -Wthinnest,gray40 -O -K >> $ps
gmt grdcontour $grd -J -R -A50+f7p,gray40 -C50 -L-100/-10 -Wthinnest,gray40 -O -K >> $ps

#EEZ Alaska
awk -F, '{print $1, $2}' $eez01  | gmt psxy -R -J -Wdefault,white,--  -O -V -K  >> $ps
#EEZ Canada
awk -F, '{print $1, $2}' $eez02  | gmt psxy -R -J -Wdefault,white,--  -O -V -K  >> $ps
#EEZ Russia
awk -F, '{print $1, $2}' $eez03  | gmt psxy -R -J -Wdefault,white,--  -O -V -K  >> $ps

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
-147 72  BEAUFORT
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0/0.1 -V -O -K <<EOF>> $ps
-147 72  BEAUFORT
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D-0/-0.2 -V -O -K <<EOF>> $ps
-147 72  SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D-0/-0.2 -V -O -K <<EOF>> $ps
-147 72  SEA
EOF

# East siberian SEA (163E, 72N)
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D+1/0.0 -V -O -K <<EOF>> $ps
163 72  EAST
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D+1/0.0 -V -O -K <<EOF>> $ps
163 72   EAST
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D+1/-0.3 -V -O -K <<EOF>> $ps
163 72   SIBERIAN
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D+1/-0.3 -V -O -K <<EOF>> $ps
163 72   SIBERIAN
EOF
gmt pstext -F+f8.p,Helvetica-Bold=thickest,white  -R -J -D+1/-0.6 -V -O -K <<EOF>> $ps
163 72  SEA
EOF
gmt pstext -F+f8.p,Helvetica-Bold,blue  -R -J -D+1/-0.6 -V -O -K <<EOF>> $ps
163 72   SEA
EOF

# Wrangelya Island
gmt pstext -F+f6p,Helvetica-Bold,black  -R -J -D0./0. -V -O -K <<EOF>> $ps
-179.41667 71.2333333 Wrangelya I.
EOF

# Bering Strait
gmt pstext -F+a88+f6p,Helvetica-Oblique,blue  -R -J -D-0./0. -V -O -K <<EOF>> $ps
-169.82833333 65.09111111  Bering Strait
EOF

# Brooks Range
gmt pstext -F+a24+f6.2p,Helvetica-Oblique,black  -R -J -D0./0.3 -V -O -K <<EOF>> $ps
-152.25 68.2  BROOKS RANGE
EOF

# Canada Basin
gmt pstext -F+a299+f7p,Helvetica-Bold=thickest,white  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
-143.27153 77.353563  CANADA BASIN
EOF
gmt pstext -F+a299+f7p,Helvetica-Bold,blue  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
-143.27153 77.353563  CANADA BASIN
EOF

# Canada Abyssal Plain
# gmt pstext -F+a289+f6.5p,Helvetica-Bold=thickest,white  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
# -150 78  CANADA ABYSSAL PLAIN
# EOF
gmt pstext -F+a289+f6.5p,Helvetica-Bold,blue  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
-150 78  CANADA ABYSSAL PLAIN
EOF

# Northwind Ridge
# gmt pstext -F+a289+f6.5p,Helvetica-Bold=thickest,white  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
# -150 78  CANADA ABYSSAL PLAIN
# EOF
gmt pstext -F+a269+f6p,Helvetica-oblique,blue  -R -J -D0.15/-0 -V -O -K <<EOF>> $ps
-157.10482 76.718071  NORTHWIND RIDGE
EOF

# Northwind ABYSSAL PLAIN
gmt pstext -F+a259+f5p,Helvetica-oblique,blue  -R -J -D-0.25/-0 -V -O -K <<EOF>> $ps
-157.2363476 77.51653299  NORTHWIND ABYSSAL PLAIN
EOF

# Chukchi Plateau
gmt pstext -F+a0+f5p,Helvetica,blue  -R -J -D0./1.1 -V -O -K <<EOF>> $ps
-166 77  CHUKCHI 
EOF
gmt pstext -F+a0+f5p,Helvetica,blue  -R -J -D0./0.8 -V -O -K <<EOF>> $ps
-166 77  PLATEAU
EOF

# Chukchi ABYSSAL PLAIN
gmt pstext -F+a0+f5p,Helvetica,blue  -R -J -D-0.2/0.25 -V -O -K <<EOF>> $ps
-172 76.75  CHUKCHI 
EOF
gmt pstext -F+a0+f5p,Helvetica,blue  -R -J -D-0.2/-0.05 -V -O -K <<EOF>> $ps
-172 76.75  ABYSSAL PLAIN
EOF

# Mendeleev ABYSSAL PLAIN
gmt pstext -F+a340+f5p,Helvetica,blue  -R -J -D0./0. -V -O -K <<EOF>> $ps
-169 81.5  MENDELEEV 
EOF
gmt pstext -F+a340+f5p,Helvetica,blue  -R -J -D0./-0.3 -V -O -K <<EOF>> $ps
-169 81.5  ABYSSAL PLAIN
EOF

# Mendeleev RIDGE
gmt pstext -F+a92+f6p,Helvetica-Bold=thickest,white  -R -J -D-0/-0.1 -V -O -K <<EOF>> $ps
-178 80  MENDELEEV  RIDGE
EOF
gmt pstext -F+a92+f6p,Helvetica-Bold,blue  -R -J -D-0/-0.1 -V -O -K <<EOF>> $ps
-178 80  MENDELEEV  RIDGE
EOF

#Kucherov Terrace
gmt pstext -F+a300+f5p,Helvetica,blue  -R -J -D0.2/0. -V -O -K <<EOF>> $ps
174.53196401 77.7192987   KUCHEROV
EOF
gmt pstext -F+a300+f5p,Helvetica,blue  -R -J -D-0.1/-0. -V -O -K <<EOF>> $ps
174.53196401 77.7192987   TERRACE
EOF
# gmt pstext -F+a39+f6.2p,Helvetica,blue  -R -J -D0./-0 -V -O -K <<EOF>> $ps
# 174.53196401 77.7192987  KUCHEROV TERRACE
# EOF

# Wrangel ABYSSAL PLAIN
gmt pstext -F+a30+f5p,Helvetica,blue  -R -J -D-0.15/0.05 -V -O -K <<EOF>> $ps
170 82.5  WRANGEL 
EOF
gmt pstext -F+a30+f5p,Helvetica,blue  -R -J -D-0.15/-0.25 -V -O -K <<EOF>> $ps
170 82.5  ABYSSAL PLAIN
EOF

# Makarov Basin (140E, 88N)
gmt pstext -F+a62+f7p,Helvetica-Bold=thickest,white  -R -J -D-0.2/-0 -N -V -O -K <<EOF>> $ps
161 82  MAKAROV BASIN
EOF
gmt pstext -F+a62+f7p,Helvetica-Bold,blue  -R -J -D-0.2/-0 -N -V -O -K <<EOF>> $ps
161 82  MAKAROV BASIN
EOF

gmt psscale -D3.55i/-0.5i/3.5i/0.15ih -C$palette -B3000f1000:"Depth (m)": -O -K -V >> $ps   

# track
awk -F, '{print $3, $2}' $data  | gmt psxy -R -J -W1p,orange,--  -O -V -K  >> $ps


# Station 1 ~ 98
awk -F, '{if (NR>1) print $3, $2}' $data | \
	gmt psxy -JS -R -Sc0.12 -Gred -Wfaint,black  -O -V -K >> $ps


# Station numbers
# 1 ~ 4
awk -F, '{if (NR>1 && NR<=5) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.10/0.06  >> $ps

# 5 ~ 10
awk -F, '{if (NR>5 && NR<=11) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.09/0.06  >> $ps

# 11 ~ 19
awk -F, '{if (NR>11 && NR<=20) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.12/0.06  >> $ps

# 20 ~ 33
awk -F, '{if (NR>20 && NR<=34) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/0.06  >> $ps

# 34 ~ 39
awk -F, '{if (NR>34 && NR<=40) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/0.06  >> $ps

# 40
awk -F, '{if (NR==41) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 41 ~ 53
awk -F, '{if (NR>41 && NR<=54) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/0.06  >> $ps

# 54 ~ 58
awk -F, '{if (NR>54 && NR<=59) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 59 
awk -F, '{if (NR==60) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/-0.06  >> $ps

# 60
awk -F, '{if (NR==63) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/-0.09  >> $ps

# 60b
gmt pstext -R -J  -F+f3p,Helvetica-Bold,dimgray+jCM  -V  -O -K -D-0.02/-0.15 <<EOF>> $ps
174.9163333 74.6363  60b
EOF

# 61
awk -F, '{if (NR==64) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 61b
gmt pstext -R -J  -F+f3p,Helvetica-Bold,dimgray+jCM  -V  -O -K -D0.18/-0.15 <<EOF>> $ps
174.93925 74.62221667  61b
EOF



# 62
awk -F, '{if (NR==65) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/-0.06  >> $ps

# 63 
awk -F, '{if (NR==66) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 64 
awk -F, '{if (NR==67) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.16/0.00  >> $ps

# 65 
awk -F, '{if (NR==68) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/0.06  >> $ps

# 66 ~ 75
awk -F, '{if (NR>68 && NR<=78) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/-0.06  >> $ps

# 76 ~ 92
awk -F, '{if (NR>78 && NR<=95) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/-0.06  >> $ps

# 93 ~ 98
awk -F, '{if (NR>95 && NR<=101) print $3, $2, $1}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/-0.06  >> $ps


# CTD DO 채수 
gmt psxy -R -J -Sc0.05 -Gyellow -Wfaint,black  -O -V -K <<EOF>> $ps
-167.89827 74.800615  # 23
EOF

# DIC 채수 
gmt psxy -R -J -Sc0.05 -Gblue -Wfaint,black  -O -V -K <<EOF>> $ps
-167.89827 74.800615  # 40
EOF

# lon lat 
# -166.542 53.8898 # Dutch Harbor

gmt psxy -R -J  -Ss0.2 -Wdefault,black -Glimegreen -V  -O -K <<EOF>> $ps
-156.788611 71.290556 # Barrow
-165.406389 64.501111 # Nome
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D0.5/0.15 -V -O -K <<EOF>> $ps
-156.788611 71.290556  Barrow
EOF

gmt pstext -R -J  -F+f6p,Helvetica,gray23  -D0.25/0.16 -V -O  <<EOF>> $ps
-165.406389 64.501111 Nome
EOF




gmt psconvert $ps -Au1. -Tg -P

open $png
rm gmt.*