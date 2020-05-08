import pygame

class MenuItem:
    
    def __init__(self,font,name,color):
        print("MenuItem created")
        self.font = font
        self.name = " "+name+" "
        self.color = color
        
        # create the text surface and add it to the object
        # so its cached
        self.textSurface = self.font.render(self.name, False, self.color)
        
    def drawItem(self,screen,x,y):
        screen.blit(self.textSurface,(x,y))
        return self.textSurface.get_width()
        