#!/bin/sh
# usage: sh make_video.sh FRAMES_DIR   -> video_cacing.mp4 (15fps, 720x1280, audio cacing.wav)
ffmpeg -y -framerate 15 -i "$1/f%05d.jpg" -i cacing.wav -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest video_cacing.mp4
