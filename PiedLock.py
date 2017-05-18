import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(16,True)
GPIO.output(12,True)
GPIO.output(10,True)
i=1
f=0
x=0
y=0
z=0
GPIO.setup(22,GPIO.IN)
a=0
while i<2:
    if(GPIO.input(16)==True):
        print "Bedroom door is open"
	f=1
	x+=1
    if (GPIO.input(12)==True):
        print "Dinning door is open"
	f=1
	y+=1
    if(GPIO.input(10)==True):
	print "Main door is open"
	f=1
	z+=1
    if (GPIO.input(22)==True):
    	print "FIRE Breakout"
        a+=1
	f+=1
    print  " "
    if(f==0): 
         print "Secured"
    else:
	 print "SECURITY BREACHED"
	 print "Fire or heat detected for ",a," second" 
         print "Dinning door was opened for ",y," seconds"
	 print "Main  door was opened for ",z," seconds"
	 print "Bedroom  door was opened for ",x," seconds" 
    time.sleep(1)
    os.system('clear')
