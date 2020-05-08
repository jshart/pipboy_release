import time
import RPi.GPIO as GPIO

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up Led pins
pin_green = 16
pin_yellow = 20
pin_red = 21

GPIO.setup(pin_green,GPIO.OUT)
GPIO.setup(pin_yellow,GPIO.OUT)
GPIO.setup(pin_red,GPIO.OUT)
GPIO.output(pin_green,GPIO.LOW)
GPIO.output(pin_yellow,GPIO.LOW)
GPIO.output(pin_red,GPIO.LOW)


print("watching...")
mainLoop = True
while mainLoop:
 
    print("LEDs off")

    # Turn off all the lights.
    GPIO.output(pin_green,GPIO.LOW)
    GPIO.output(pin_yellow,GPIO.LOW)
    GPIO.output(pin_red,GPIO.LOW)

    time.sleep(1.0)
    
    GPIO.output(pin_red,GPIO.HIGH)
    GPIO.output(pin_yellow,GPIO.HIGH)
    GPIO.output(pin_green,GPIO.HIGH)
    print("LEDS on")
        
    
#text = input("Press return to quit...")

#print("Final position was {}".format(rotaryPosition))
