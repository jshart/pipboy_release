import pygame
import os
#import noise

screenX=480
screenY=320

pygame.font.init()

pygame.init()
screen = pygame.display.set_mode((screenX,screenY))

pygame.draw.rect(screen,(255,0,0),(20,20,20,20),1)

pygame.display.update()
