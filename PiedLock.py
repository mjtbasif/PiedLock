import RPi.GPIO as GPIO
import time
import os

import smtplib

from twilio.rest import Client


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
msg=''
tempBody=''
BedMsg='Left room window is open'
DinningMsg='Main door is open'
MainMsg='Right window is open'
FireMsg='Fiire breakout'
while i<2:
    if(GPIO.input(16)==True):
        print BedMsg
        tempBody=tempBody+BedMsg+'\n'
        mFlag=1
	f=1
	x+=1
    if (GPIO.input(12)==True):
        print DinningMsg
        tempBody=tempBody+DinningMsg+'\n'
        mFlag=1
	f=1
	y+=1
    if(GPIO.input(10)==True):
	print MainMsg
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
         print "Right window was opened for",y," seconds"
	 print "Left window  was opened for ",z," seconds"
	 print "Main door  was opened for ",x," seconds" 

    if(mFlag):
        if(msg!=tempBody):
            msg=tempBody
	    tempBody=''
	    
            mailUser='username@gmail.com'
            mailPass='password'

            toAdd='my mail'
            fromAdd=mailUser

            subject='PiedLock: Alert'
            header='To: '+toAdd+'\n'+'From: '+fromAdd+'\n'+'Subject: '+subject

            print header+'\n'+msg

            s=smtplib.SMTP('smtp.gmail.com',587)
            s.ehlo()
            s.starttls()
            s.ehlo()

            s.login(mailUser,mailPass)
            s.sendmail(fromAdd,toAdd,header+'\n\n'+msg)
            s.quit()
	    # Your Account SID from twilio.com/console
	    account_sid = "account sid"
            # Your Auth Token from twilio.com/console
            auth_token  = "auth token"

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                     to="user number", 
                                     from_="my number",
                                     body=msg)

            print("Message sent")
            
            mFlag=0
        else:
            tempBody=''
    time.sleep(1)
    os.system('clear')
