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

pygame.font.init()
menuFontSize=20
menuFont = pygame.font.SysFont('Courier New', menuFontSize)
bodyFontSize=16
bodyFont = pygame.font.SysFont('Courier New', bodyFontSize)

def drawTestScreen(s,f):
    global menuFontSize
    global screenX
    global screenY
    lineNum=0
    pygame.draw.rect(s,dColor,(0,menuFontSize,screenX,screenY-menuFontSize),5)
    str="---------1---------2---------3---------4"
    textSurface = f.render(str, False, dColor)
    lineNum+=1
    s.blit(textSurface,(5,menuFontSize*lineNum))

    str="1234567890123456789012345678901234567890"
    textSurface = f.render(str, False, dColor)
    lineNum+=1
    s.blit(textSurface,(5,menuFontSize*lineNum))

    str="R:{},{}".format(screenX,screenY-menuFontSize)
    textSurface = f.render(str, False, dColor)
    lineNum+=1
    s.blit(textSurface,(5,menuFontSize*lineNum))

    str="F:{}".format(menuFontSize)
    textSurface = f.render(str, False, dColor)
    lineNum+=1
    s.blit(textSurface,(5,menuFontSize*lineNum))


pygame.init()
screen = pygame.display.set_mode((screenX,screenY))
screensPath="UIScreens"

drawTestScreen(screen,menuFont)

pygame.display.update()

pygame.image.save(screen,os.path.join(screensPath,"DATA.png"))
pygame.quit()
sys.exit()
exit()
