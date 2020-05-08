import pygame
import os


class PipboyScreen:
    
    def __init__(self,font,name,color):
        print("Pipboy Screen created")
        self.font = font
        self.name = name
        self.color = color
        self.text = []
        self.gfxImage = None

    def loadScreenUsingTextFile(self,pathname):
        filename=os.path.join(pathname,self.name+".txt")
        print("looking for: "+filename)
        
        if os.path.exists(filename) == True:
            # file exists, so load it - its not an error
            # for it to not exist (as it just means this
            # screen doesnt have associated text
            print("Found: "+filename)
            rawfile=open(filename,"r")

            if rawfile.mode == 'r':
                contents=rawfile.readlines()
                for str in contents:
                    str=str[:-1]
                    self.text.append(str)
        else:
            print("Not found: "+filename)
                

    def loadScreenUsingGfxFile(self,pathname):
        filename=os.path.join(pathname,self.name+".png")
        print("looking for: "+filename)
        
        if os.path.exists(filename) == True:
            print("Found: "+filename)
            # file exists, so load it - its not an error
            # for it to not exist (as it just means this
            # screen doesnt have associated gfx file
            self.gfxImage = pygame.image.load(os.path.join(filename))
        else:
            print("Not found: "+filename)
        
    def drawScreen(self,screen,font,xoffset,yoffset,menuOffset):
        # check for image existence first
        if self.gfxImage is not None:
            screen.blit(self.gfxImage,(xoffset,(menuOffset+1)+yoffset))

        lineNum=0
        # If we have any text go ahead and convert them to
        # text surfaces so we can blit them onto the screen
        for str in self.text:
            textSurface = font.render(str, False, self.color)
            screen.blit(textSurface,(0,menuOffset+(self.font.get_linesize()*lineNum)+yoffset))
            lineNum+=1
