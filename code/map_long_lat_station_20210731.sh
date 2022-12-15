#!/bin/bash
cd /Users/jung-ok/work1/geodata/grds

gmt gmtset IO_SEGMENT_MARKER ">"
gmt gmtset FORMAT_GEO_MAP F MAP_FRAME_TYPE plain PS_MEDIA b4
gmt gmtset PS_PAGE_ORIENTATION portrait
gmt gmtset MAP_GRID_PEN_PRIMARY dimgray,...

# Input file, Output file
ps='/Users/jung-ok/work1/ARA12B/figure/ARA12B_station_1_95.ps'
png='/Users/jung-ok/work1/ARA12B/figure/ARA12B_station_1_95.png'

palette='/Users/jung-ok/work1/geodata/palette/colombia.cpt'
grd='/Users/jung-ok/work1/geodata/grds/ETOPO/ETOPO1_Bed_g_gmt4.grd'
nc='/Users/jung-ok/work1/geodata/grds/ETOPO/etopo1-int.nc'

data='/Users/jung-ok/work1/ARA12B/stationinfo/ARA12B_long_lat_station_20210731.csv'

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
gmt pstext -F+a289+f6.5p,Helvetica-Bold,blue  -R -J -D-0/-0 -V -O -K <<EOF>> $ps
-150 78  CANADA ABYSSAL PLAIN
EOF

# Northwind Ridge
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
awk -F, '{print $1, $2}' $data  | gmt psxy -R -J -W1p,orange,--  -O -V -K  >> $ps


### DIC 채수 
# gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K <<EOF>> $ps
# -167.89827 74.800615  # 40
# EOF

# No. 1, St.023
awk -F, '{if (NR==24) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 2, St.033
awk -F, '{if (NR==34) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 3, St.040
awk -F, '{if (NR==41) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 4, St.041
awk -F, '{if (NR==42) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 5, St.045
awk -F, '{if (NR==46) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 6, St.048 ~ St.049  
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K <<EOF>> $ps
173.923808 76.7318567 
EOF

# No. 7, St.056  
awk -F, '{if (NR==57) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 8, St.081  
awk -F, '{if (NR==85) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 9, St.087  
awk -F, '{if (NR==91) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps

# No. 10, St.95  
awk -F, '{if (NR==99) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.28 -Gyellow -Wfaint,black  -O -V -K >> $ps


### CTD DO 채수 
# gmt psxy -R -J -Sc0.20 -Gblue -Wfaint,black  -O -V -K <<EOF>> $ps
# -167.89827 74.800615  # 23
# EOF

# No. 1, St.023
awk -F, '{if (NR==24) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.20 -Ggreen -Wfaint,black  -O -V -K >> $ps

# No. 2, St.034
awk -F, '{if (NR==35) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.20 -Ggreen -Wfaint,black  -O -V -K >> $ps

# No. 1, St.061
awk -F, '{if (NR==65) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.20 -Ggreen -Wfaint,black  -O -V -K >> $ps

# No. 2, St.082
awk -F, '{if (NR==86) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.20 -Ggreen -Wfaint,black  -O -V -K >> $ps

# No. 2, St.091
awk -F, '{if (NR==95) print $1, $2}' $data | 
gmt psxy -R -J -Sc0.20 -Ggreen -Wfaint,black  -O -V -K >> $ps


### 정점 표시 Station 1 ~ 98

# CTD
awk -F, '{if (NR>1 && $4>2) print $1, $2}' $data | \
	gmt psxy -JS -R -Sc0.12 -Gblack -Wfaint,black  -O -V -K >> $ps

# CTD only
awk -F, '{if (NR>1 && $4<=2) print $1, $2}' $data | \
	gmt psxy -JS -R -Sc0.12 -Gred -Wfaint,black  -O -V -K >> $ps    




# (CTD) + (CTD only)
# awk -F, '{if (NR>1) print $1, $2}' $data | \
# 	gmt psxy -JS -R -Sc0.12 -Gred -Wfaint,black  -O -V -K >> $ps    

# Station numbers
# 1 ~ 4
awk -F, '{if (NR>1 && NR<=5) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.10/0.06  >> $ps

# 5 ~ 10
awk -F, '{if (NR>5 && NR<=11) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.09/0.06  >> $ps

# 11 ~ 19
awk -F, '{if (NR>11 && NR<=20) print $1, $2, $3}' $data | 
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

# WP1
awk -F, '{if (NR==59) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM -V  -O -K -D-0.1/-0.12  >> $ps

# WP2
awk -F, '{if (NR==60) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM -V  -O -K -D0.15/-0.05  >> $ps

# 58H
awk -F, '{if (NR==61) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM   -V  -O -K -D0.2/0.05  >> $ps

# 58I
awk -F, '{if (NR==62) print $1, $2, $3}' $data | 
gmt pstext -R -J   -F+f3p,Helvetica-Bold,dimgray+jCM   -V  -O -K -D-0.14/0.06  >> $ps

# 59 ~ 60
awk -F, '{if (NR>62 && NR<=64) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.13/0.06  >> $ps

# 61 ~ 62
awk -F, '{if (NR>64 && NR<=66) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.0/0.13  >> $ps

# 63 ~ 65
awk -F, '{if (NR>66 && NR<=69) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0./-0.13  >> $ps

# 66 ~ 69
awk -F, '{if (NR>69 && NR<=73) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0./-0.13  >> $ps

# 70
awk -F, '{if (NR==74) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.15/-0.  >> $ps

# 71
awk -F, '{if (NR==75) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0./0.13  >> $ps

# 72
awk -F, '{if (NR==76) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.15/-0.  >> $ps

# 73 ~ 84
awk -F, '{if (NR>76 && NR<=88) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0.14/-0.06  >> $ps

# 85 ~ 90
awk -F, '{if (NR>88 && NR<=94) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.14/-0.06  >> $ps

# 91 ~ 92
awk -F, '{if (NR>94 && NR<=96) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0./-0.13  >> $ps

# 93
awk -F, '{if (NR==97) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0./-0.13  >> $ps

# 94
awk -F, '{if (NR==98) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D-0./-0.13  >> $ps

# 95
awk -F, '{if (NR==99) print $1, $2, $3}' $data | 
gmt pstext -R -J  -F+f4p,Helvetica-Bold,black+jCM  -V  -O -K -D0.15/-0  >> $ps

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

### legend

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

gmt pslegend -R -J -O -Dx4.5i/0/1.3i/TR -X-3.0i -Y5.2i -F+p+glightyellow >> $ps << EOF 
S 0.15i c 0.12 red 0.25p 0.3i CTD Only
S 0.15i c 0.12 black 0.25p 0.3i CTD
S 0.15i c 0.20 green 0.25p 0.3i DO
S 0.15i c 0.28 yellow 0.25p 0.3i DIC
EOF

gmt psconvert $ps -Au1. -Tg -P
open $png
rm gmt.*