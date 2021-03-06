#  This program use a L298N Dual Motor Controller(module)
#
#  Use BOARD NUMBER !
#  ------------------
#
#  RIGHT FORWARD --> Pin 16
#  RIGHT REVERSE --> Pin 18
#  LEFT  FORWARD --> Pin 11
#  LEFT  REVERSE --> Pin 13
#

import RPi.GPIO as GPIO		#import GPIO Library
import time			#import time Library
import getch			#import single-char input Library

GPIO.setmode(GPIO.BOARD)	#GPIO -board number 
GPIO.setwarnings(False)		#Disable messages

F_RIGHT = 16			#set GPIO pins of motor
F_LEFT = 11
R_RIGHT = 18
R_LEFT = 13

def initialization():		#set pins as output	
  GPIO.setup(F_LEFT,GPIO.OUT)	
  GPIO.setup(R_LEFT,GPIO.OUT)		
  GPIO.setup(F_RIGHT,GPIO.OUT)	
  GPIO.setup(R_RIGHT,GPIO.OUT)

def move_stop():			#stop ALL
  GPIO.output(F_LEFT,GPIO.LOW)	
  GPIO.output(R_LEFT,GPIO.LOW)	
  GPIO.output(F_RIGHT,GPIO.LOW)
  GPIO.output(R_RIGHT,GPIO.LOW)	

def move_foward():		#Move Forward
  GPIO.output(F_RIGHT,GPIO.HIGH)		
  GPIO.output(F_LEFT,GPIO.HIGH)		
  time.sleep(0.4)
  GPIO.output(F_RIGHT,GPIO.LOW)		
  GPIO.output(F_LEFT,GPIO.LOW)		
      
def move_reverse():		#Move Reverse
  GPIO.output(R_RIGHT,GPIO.HIGH)		
  GPIO.output(R_LEFT,GPIO.HIGH)		
  time.sleep(0.4)
  GPIO.output(R_RIGHT,GPIO.LOW)	
  GPIO.output(R_LEFT,GPIO.LOW)

def move_right():		#Move Right
  GPIO.output(F_LEFT,GPIO.HIGH)
  time.sleep(0.2)
  GPIO.output(F_LEFT,GPIO.LOW)

def move_left():			#Move Left
  GPIO.output(F_RIGHT,GPIO.HIGH)		
  time.sleep(0.2)
  GPIO.output(F_RIGHT,GPIO.LOW)	


initialization()

print("""\

|------------------|
|    CONTROLS:     |
|   __      __     |
|   \ \ /\ / /     |
|    \ V  V /      |
|     \_/\_/       |
|               _  |
|  __ _ ___  __| | |
| / _` / __|/ _` | |
| |(_| \__ \ (_| | |
| \__,_|___/\__,_| |
|                  |
| o --> stop ALL   |
| q --> quit       |
|------------------|

""")


while True:				# Control KEYS motor
  input_key= getch.getch()
  if input_key == 'w':
    move_foward()
  elif input_key == 's':
    move_reverse()
  elif input_key == 'd':
    move_right()
  elif input_key == 'a':
    move_left()
  elif input_key == 'o':
    move_stop()
  elif input_key == 'q':
    print ('Goodbye!')
    exit()
