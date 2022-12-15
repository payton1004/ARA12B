#!/bin/bash
cd /Users/jung-ok/work1/ARA12B/figure/sic/daily/


# animated gif
# identify ; to get information about an image (picture)
# convert -adjoin -dispose previous -delay 100 -loop 0 -layers Optimize *week*.pdf anim.gif
# convert -dispose previous -delay 100 -loop 0 -layers Optimize -alpha remove *.pdf anim.gif
convert -dispose previous -delay 100 -loop 0 -layers Optimize -alpha remove *.png anim.gif

# mkdir frames
# into frames
convert -coalesce anim.gif ./frames/frames%04d.png

# # movie 
# # ffmpeg -formats
# # ffmpeg -codecs
# # ffmpeg -h encoder=mpeg4
# # ffmpeg -h encoder=h264
# ffmpeg -i ./frames2/frames%04d.png -vcodec libx264 -pix_fmt yuv420p  -y  original.m4v
ffmpeg -i ./frames/frames%04d.png -vcodec libx264 -vf scale=1280:-2 -pix_fmt yuv420p  -y  original.m4v
# # slowing down a video
# ffmpeg -i original.m4v -filter:v "setpts=10.0*PTS" slow.m4v
ffmpeg -i original.m4v -filter:v "setpts=30.0*PTS" slow.m4v