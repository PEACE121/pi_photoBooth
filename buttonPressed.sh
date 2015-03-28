#!/bin/bash

./usbreset /dev/bus/usb/001/014
gphoto2 --capture-image-and-download --filename shots/shot_%y%m%d%H%M%S.jpg
processFeh=$(pidof feh)
echo "instance: $processFeh"
/usr/bin/feh --hide-pointer --quiet --recursive --reverse --sort name --full-screen --slideshow-delay 5 'shots' &
sleep 10 && kill $processFeh &

