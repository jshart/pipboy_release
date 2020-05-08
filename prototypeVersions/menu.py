import threading
import time
import pygame

# Init the display and setup for gfx
pygame.init()
#screen = pygame.display.set_mode((400,300), pygame.FULLSCREEN)
screen = pygame.display.set_mode((400,300))

pygame.font.init()
myFont = pygame.font.SysFont('Courier New', 30)

menu = ["foo", "bar", "man", "cho"]
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

print("watching...")
mainLoop = True
while mainLoop:
    time.sleep(0.01)
 
    # Check for any pygame events, and react if any
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
    
    # clear the screen and draw a circle at a new position
    screen.fill((0,0,0))
    
#    if menuItem >= 0 and menuItem <4:
#        drawSelectedMenu(screen,myFont, menu[menuItem])
#    else:
#        pygame.draw.circle(screen, (100,100,100), (50,50), 10)
        
    # redraw the menu and update the game engine
    drawMenu(screen,myFont,menu,menuItem)
    pygame.display.update()
    
    # invite the user to select a menu item and convert
    # it to a number so we know which item to enact in the UI
    text = input("Select Menu Option...")
    print("Menu Item selected:{}".format(text))
    menuItem=int(text)
    
    if text == "q":
        mainLoop = False;



#print("Final position was {}".format(rotaryPosition))
    