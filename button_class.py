import pygame

class Button(object):
    def __init__(self, x, y, w, h, size, text, color):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.size = size
        self.text = text
        self.color = color
        
    def draw(self, screen):  # draws centralised buttons and text
        font = pygame.font.Font(None,self.size)
        textSurface = font.render(self.text,True,(255,255,255))
        textRect = textSurface.get_rect()
        buttonRect = pygame.Rect(self.x,self.y,self.width,self.height)
        textRect.center = buttonRect.center

        pygame.draw.rect(screen,self.color,buttonRect)
        screen.blit(textSurface,textRect)

    def isOver(self, pos):  ## detects if mouse positions is above buttons'
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
