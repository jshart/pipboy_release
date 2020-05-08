import pygame
import os
import sys
from greenFilter import remap

screenX=480
screenY=320
graphBase=screenY-40
graphSide=screenX-5
halfWidth = int(screenX/2)
graphSideB = halfWidth-(5+10)
dR=60
dG=243
dB=170
dColor = (dR,dG,dB)

pygame.init()
screen = pygame.display.set_mode((screenX,screenY))
screensPath="UIScreens"

#i = pygame.image.load(os.path.join(screensPath,'rawMap.png')).convert()


#remap(i)

#screen.blit(i,(0,0))

# X axis
pygame.draw.line(screen,dColor,(halfWidth,graphBase),(graphSide,graphBase),1)
barH=0
for i in range(halfWidth,graphSide,5):
    if i % 20 == 0:
        barH=10
    else:
        barH=5
    pygame.draw.line(screen,dColor,(i,graphBase),(i,graphBase-barH),1)    

# Y axis
pygame.draw.line(screen,dColor,(graphSide,25),(graphSide,graphBase),1)
barH=0
for i in range(25,graphBase,5):
    if i % 20 == 0:
        barH=10
    else:
        barH=5
    pygame.draw.line(screen,dColor,(graphSide,i),(graphSide-barH,i),1)  

pygame.display.update()

pygame.image.save(screen,os.path.join(screensPath,"graph.png"))
pygame.quit()
sys.exit()
exit()
