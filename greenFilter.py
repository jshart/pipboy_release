import pygame
import os
import sys

def domColor(r,g,b):
    result = 0
    if r>result:
        result=r
    if g>result:
        result=g
    if b>result:
        result=b
    return b

def averageColor(r,g,b):
    result = (r+g+b)/3
    return int(result)

def remap(i):
    w = i.get_width()
    h = i.get_height()
    for wp in range(w):
        for wh in range(h):
            pc = i.get_at((wp,wh))

            pc.g = 255-domColor(pc.r,pc.g,pc.b)
            #pc.g = averageColor(pc.r,pc.g,pc.b)
            greenRatio = pc.g/255
            pc.a = 255
            if pc.g>0:
                pc.r = int(60 * greenRatio)
                pc.b = int(170 * greenRatio)
            else:
                pc.r = 0
                pc.b = 0

            i.set_at((wp,wh),pc)
