import pygame

class Key:
    def __init__(self,x,y,width,height,letter):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,width,height)
        self.letter = letter
        self.color = "#e8e8e8"
        

    ## Changes color based on status
    def changeColor(self,status):
        if status == "empty":
            self.color = "#e8e8e8"
        elif status == "correct":
            self.color = "#02a102"
        elif status == "partial":
            self.color = "#ffa500"
        else:
            self.color = "#575757"


    ## Draws box & letter
    def drawBox(self, screen):
        ## Define the text
        font = pygame.font.Font(None,30)    ## create font object
        textSurface = font.render(self.letter,True,(255,255,255))   ## Render the text
        textRect = textSurface.get_rect()   ## Get rect object for text
        textRect.center = self.rect.center ## Center text in the box

        ## Draw text & box
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(textSurface,textRect)
