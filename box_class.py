import pygame

class Box:
    def __init__(self,x,y,width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,width,height)
        self.letter = ""
        self.color = "#e8e8e8"
        self.status = "empty"


    ## Changes color based on status
    def changeColor(self):
        if self.status == "empty":
            self.color = "#e8e8e8"
        elif self.status == "correct":
            self.color = "#00ff00"
        elif self.status == "partial":
            self.color = "#ffa500"
        else:
            self.color = "#575757"

        
    ## Deletes letter
    def deleteLetter(self):
        self.letter = ""
        self.status = "empty"


    ## Draws box & letter
    def drawBox(self, screen):
        ## Define the text
        font = pygame.font.Font(None,36)    ## create font object
        textSurface = font.render(self.letter,True,(255,255,255))   ## Render the text
        textRect = textSurface.get_rect()   ## Get rect object for text
        textRect.center = self.rect.center ## Center text in the box

        ## Draw text & box
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(textSurface,textRect)


    ## Updates letter
    def writeLetter(self,letter):
        self.letter = letter.upper()

