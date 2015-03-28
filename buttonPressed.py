#!/usr/bin/env python

os.system("./usbreset /dev/bus/usb/001/014")
os.system("gphoto2 --capture-image-and-download --filename '%s/shot_%%y%%m%%d%%H%%M%%S.jpg'" % timestring)
proc = subprocess.Popen(['/usr/bin/feh', '--hide-pointer', '--quiet', '--recursive', '--reverse', '--sort', 'name', '--full-screen', '--slideshow-delay', '5', timestring])	
sleep(10)
try:	
	procOld.kill()
except NameError:
	print "procOld does not exist"	
procOld = proc	
