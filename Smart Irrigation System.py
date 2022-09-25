import sys                  
import RPi.GPIO as GPIO 
import serial               
from time import sleep
import pyrebase 
import ntplib
from datetime import datetime
import random

config = {     
  "apiKey": "knkbQNwRc1NPXQLcMc4M6Gu0aERxnL6Ahhom5V7d",
  "authDomain": "irrigation.firebaseio.com",
  "databaseURL": "https://irrigation-3d6f9-default-rtdb.firebaseio.com",
  "storageBucket": "irrigation.appspot.com"
}

firebase = pyrebase.initialize_app(config)
U1 = 26
U2 = 5

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)
GPIO.setup(U1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(U2, GPIO.OUT)

ProjectBucket = firebase.database()

try:
    while True:
        try:
            ntp_client = ntplib.NTPClient()
            response = ntp_client.request('pool.ntp.org')
            
        except:
            #print("Door")
            if GPIO.input(U1) == GPIO.LOW:
                ProjectBucket.child("/U1").set("Dry")
                print("Dry")
                GPIO.output(U2, False)
            else:
                ProjectBucket.child("/U1").set("Wet")
                print("Wet")
                GPIO.output(U2, True)
           
except KeyboardInterrupt:
    GPIO.cleanup()            
    #sys.exit(0)