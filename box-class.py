import pygame

class box:
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,width,height)
        self.letter = ""
        self.color = "#e8e8e8"
        self.status = "empty"
