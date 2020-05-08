from pyky040 import pyky040
import threading
import time
import pygame
import RPi.GPIO as GPIO
import sys

screenX=480
#screenY=320
screenY=250

pygame.font.init()
myFont = pygame.font.SysFont('Courier New', 30)

menu = ["foo", "bar", "man", "cho","atm"]
menuItem = 0


# Generate the text for a given menu item
# Currently unused
def drawSelectedMenu(s,f, menuItem):
    #global screen
    pygame.draw.circle(s, (0,255,0),(60,60), 20)
    textSurface = f.render(menuItem, False, (0,255,0))
    s.blit(textSurface,(60,80))

# draw the entire menu and high light the selected item
def drawMenu(s,f,menu,hlItem):
    yoffset=0
    miHeight=40;
    miWidth=100;
    for i in range(0,len(menu)):
        item=menu[i]
        if (i==hlItem):
            w=5
        else:
            w=1
        pygame.draw.rect(s,(0,255,0),(1,yoffset,miWidth,miHeight),w)
        drawMenuItem(s,f,item,yoffset)
        yoffset+=miHeight
        
# render the text for a particular menu item and blit
# the rendered image onto the screen
def drawMenuItem(s,f, menuItem,yoffset):
    #global screen
    textSurface = f.render(menuItem, False, (0,255,0))
    s.blit(textSurface,(1,yoffset))

# render the text for a status bar
def drawStatusBar(s,f, status):
    #global screen
    textSurface = f.render(status, False, (0,255,0))
    s.blit(textSurface,(0,screenY-40))

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Default rotary position
rotaryPosition=0
oldRotaryPosition=0

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

encoder.setup(scale_min=0,scale_max=len(menu)-1, loop=False, step=1, sw_debounce_time=100, chg_callback=turned, sw_callback=encoderClicked)

encoderThread = threading.Thread(target=encoder.watch)
encoderThread.start()

#encoder.watch()

# Init the display and setup for gfx
pygame.init()
#screen = pygame.display.set_mode((screenX,screenY), pygame.FULLSCREEN)
screen = pygame.display.set_mode((screenX,screenY))



print("watching...")
timestamp = time.monotonic();
firstTimestamp = True
iteration = 0

clock = pygame.time.Clock()


mainLoop = True
while mainLoop:
    oldRotaryPosition=rotaryPosition
    #time.sleep(0.1)

 
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
    
    # Check for any pygame events, and react if any
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                mainLoop = False
                print("escape or space pressed")
    
    # clear the screen and draw a circle at a new position
    screen.fill((0,0,0))
  
  
#    if rotaryPosition > oldRotaryPosition:
#        menuItem+=1
#    elif rotaryPosition< oldRotaryPosition:
#        menuItem-=1
#        
#    if menuItem >= len(menu):
#        menuItem=0
#        
#    if menuItem < 0:
#        menuItem = len(menu) -1

    menuItem=rotaryPosition;

    # Create a statusbar
    newTimestamp=time.monotonic()
    timeDelta = newTimestamp - timestamp;
    iteration = iteration+1
    if iteration>=10:
        iteration=0
        
    if (firstTimestamp==True):
        rollingAverage=timeDelta
        firstTimestamp=False
    else:
        rollingAverage = (rollingAverage + timeDelta)/2
    
    statusBar="T:{:0.3f}A:{:0.3f}I:{:d}R:{:d}OR:{:d}".format(timeDelta,rollingAverage,iteration,rotaryPosition,oldRotaryPosition)
    timestamp=newTimestamp

    # redraw the menu and update the game engine
    #drawMenu(screen,myFont,menu,menuItem)
    #drawStatusBar(screen,myFont,statusBar)
    #pygame.display.update()
    #clock.tick(60)
    
        
pygame.quit()
sys.exit()
exit()
#TODO need to clean up the hanging rotary encoder thread
