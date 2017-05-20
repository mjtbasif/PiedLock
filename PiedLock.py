import RPi.GPIO as GPIO
import time
import os

import smtplib

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
mFlag=0
body=''
tempBody=''
BedMsg='Bedroom door is open'
DinningMsg='Dinning door is open'
MainMsg='Main door is open'
FireMsg='Fiire breakout'
while i<2:
    if(GPIO.input(16)==True):
        print "Bedroom door is open"
        tempBody=tempBody+BedMsg+'\n'
        mFlag=1
	f=1
	x+=1
    if (GPIO.input(12)==True):
        print "Dinning door is open"
        tempBody=tempBody+DinningMsg+'\n'
        mFlag=1
	f=1
	y+=1
    if(GPIO.input(10)==True):
	print "Main door is open"
	tempBody=tempBody+MainMsg+'\n'
	mFlag=1
	f=1
	z+=1
    if (GPIO.input(22)==True):
    	print "FIRE Breakout"
    	tempBody=tempBody+FireMsg+'\n'
    	mFlag=1
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

    if(mFlag):
        if(body!=tempBody):
            body=tempBody
	    tempBody=''
	    
            mailUser='username@gmail.com'
            mailPass='password'

            toAdd='recipientUsername@gmail.com'
            fromAdd=mailUser

            subject='PiedLock: Alart'
            header='To: '+toAdd+'\n'+'From: '+fromAdd+'\n'+'Subject: '+subject

            print header+'\n'+body

            s=smtplib.SMTP('smtp.gmail.com',587)
            s.ehlo()
            s.starttls()
            s.ehlo()

            s.login(mailUser,mailPass)
            s.sendmail(fromAdd,toAdd,header+'\n\n'+body)
            s.quit()
            
            mFlag=0
        else:
            tempBody=''
    time.sleep(1)
    os.system('clear')
