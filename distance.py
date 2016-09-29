#  This program use a Ultrasonic Module HC-SR04
#
#  Use BOARD NUMBER !
#  ------------------
#
#  TRIGGER --> Pin 31
#  ECHO    --> Pin 29
#

import RPi.GPIO as GPIO		#import GPIO Library
import time			#import time Library

GPIO.setmode(GPIO.BOARD)	#GPIO -board number 
GPIO.setwarnings(False)		#Disable messages

def Initialization():		#set pins as output	
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.IN)		

def Distance():
    GPIO.output(29,GPIO.HIGH)
    time.sleep (0.000010)
    GPIO.output(29,GPIO.LOW)
    while GPIO.input(31) == 0:
        TriggerStart = time.time()
    while GPIO.input(31) == 1:
        TriggerEnd = time.time()
    Trigger = TriggerEnd - TriggerStart
    Distance = Trigger / 0.000058
    Distance = round(Distance,2)
    print (Distance, "cm")

Initialization()

while True:
    Distance()
    time.sleep(1)