from pyky040 import pyky040
import threading
import time
import pygame
import RPi.GPIO as GPIO

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Default rotary position
rotaryPosition=0

# Call back function for encoder
def turned(scale_position):
    global rotaryPosition
    print("tuned to {}".format(scale_position))
    rotaryPosition=scale_position
    
def encoderClicked():
    print("encoder clicked")
    
def buttonPressed(channel):
    print("Button {} was pressed".format(channel))

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

# Setup the buttons
pin_BTN1 = 12
pin_BTN2 = 5


GPIO.setup(pin_BTN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin_BTN1,GPIO.RISING,callback=buttonPressed, bouncetime=500)

GPIO.setup(pin_BTN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin_BTN2,GPIO.RISING,callback=buttonPressed, bouncetime=500)


# Set up encoder details    
pin_sw = 19
pin_dt = 13
pin_clk = 6

pin_3v3 = 26

GPIO.setup(pin_3v3,GPIO.OUT)
GPIO.output(pin_3v3,GPIO.HIGH) 
encoder = pyky040.Encoder(CLK=pin_clk, DT=pin_dt, SW=pin_sw)

encoder.setup(scale_min=0,scale_max=100, step=1, chg_callback=turned, sw_callback=encoderClicked)

encoderThread = threading.Thread(target=encoder.watch)
encoderThread.start()

#encoder.watch()

# Init the display and setup for gfx
pygame.init()
#screen = pygame.display.set_mode((400,300), pygame.FULLSCREEN)
screen = pygame.display.set_mode((400,300))



print("watching...")
mainLoop = True
while mainLoop:
    time.sleep(0.01)
 
    # Turn off all the lights.
    GPIO.output(pin_green,GPIO.LOW)
    GPIO.output(pin_yellow,GPIO.LOW)
    GPIO.output(pin_red,GPIO.LOW)
    
    # Check which light to turn on and then
    # activate it
    ledToLight = rotaryPosition % 3
    
    if ledToLight == 2:
        GPIO.output(pin_red,GPIO.HIGH)
        #print("red on")
    elif ledToLight == 1:
        GPIO.output(pin_yellow,GPIO.HIGH)
        #print("yellow on")
    elif ledToLight == 0:
        GPIO.output(pin_green,GPIO.HIGH)
        #print("green on")
    #else:
        #print("position is {}".format(rotaryPosition))
    
    # Check for any pygame events, and react if any
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
    
    # clear the screen and draw a circle at a new position
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (100,100,100), (rotaryPosition,50), 10)
    pygame.display.update()
  

        
        
#text = input("Press return to quit...")
#print("Final position was {}".format(rotaryPosition))