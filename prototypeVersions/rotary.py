import pygame
from gpiozero import Button, LED

pygame.init()

pin_sw = 19
pin_dt = 13
pin_clk = 6

pin_3v3 = 26

# hack to set pin high
led = LED(pin_3v3)
led.on()

button_sw = Button(pin_sw,pull_up=True)
button_dt = Button(pin_dt,pull_up=True)
button_clk = Button(pin_clk,pull_up=True)

circleX=25
circleY=25

def sw_pressed():
    if button_sw.is_pressed: print("SW")   
    
def dt_turned():
    if button_clk.is_pressed: print("+1")
    global circleX
    circleX+=4
    
def clk_turned():
    if button_dt.is_pressed: print("-1")
    global circleX
    circleX-=4
    
button_sw.when_pressed = sw_pressed
button_dt.when_pressed = dt_turned
button_clk.when_pressed = clk_turned

#screen = pygame.display.set_mode((400,300), pygame.FULLSCREEN)
screen = pygame.display.set_mode((400,300))


mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (100,100,100), (circleX,circleY), 10)
    pygame.display.update()
    #print(circleX)
        
        
pygame.quit()

input("Turn/press the knob, return to quit")