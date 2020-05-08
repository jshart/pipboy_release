import pygame
import os
import noise
import time

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

pygame.init()
screen = pygame.display.set_mode((screenX,screenY))
screensPath="../UIScreens"

scale = 100.0
octaves = 4# tunable, but makes negliable difference to performance
persistence = 0.5
lacunarity = 2.0

ybaseline=screenY/2

totalNoise=0
totalDraw=0
timeStamp=0



graphBackground = pygame.image.load(os.path.join(screensPath,'graph.png')).convert()
screen.blit(graphBackground,(0,0))

for j in range (0,600):
    #screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,0,0),(halfWidth,ybaseline-50,graphSideB,100))
    for i in range (halfWidth,460,4):
        timeStamp=time.monotonic_ns();
        
        n = noise.pnoise2(j/scale,i/scale,octaves=octaves,persistence=persistence,lacunarity=lacunarity,repeatx=480,repeaty=480,base=0)
        afterNoise=time.monotonic_ns();
        
        offset=n*100
        pygame.draw.line(screen,dColor,(i,ybaseline+offset-3),(i,ybaseline+offset),1)
        afterDraw=time.monotonic_ns();
        #pygame.draw.line(screen,(0,255,0),(i,ybaseline/2),(i,(ybaseline/2)+offset),1)

        totalNoise=totalNoise+(afterNoise-timeStamp)
        totalDraw=totalDraw+(afterDraw-afterNoise)

        #n = noise.pnoise2(i/scale,j/scale,octaves=octaves,persistence=persistence,lacunarity=lacunarity,repeatx=512,repeaty=512,base=0)
        offset=n*100
        #pygame.draw.line(screen,(0,125,0),(i,ybaseline+offset-1),(i,ybaseline+offset),1)
        #pygame.draw.line(screen,(0,125,0),(i,ybaseline+(ybaseline/2)),(i,ybaseline+(ybaseline/2)+offset),1)
        
        #print(n)
        
    pygame.draw.line(screen,(255,0,0),((j%graphSideB)+halfWidth,ybaseline-50),((j%graphSideB)+halfWidth,ybaseline+50),1)
    pygame.display.update((0,ybaseline-100,screenX,ybaseline+100))
    time.sleep(0.01)
    
print("Noise:{:d} Draw:{:d}".format(totalNoise, totalDraw))
print("Average Noise:{:f} Average Draw:{:f}".format(totalNoise/(480*480),totalDraw/(480*480)))
      

