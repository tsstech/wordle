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


    ## Changes color based on status
    def changeColor(self):
        if status == "empty":
            self.color = "#e8e8e8"
        elif status == "correct":
            self.color = "#00ff00"
        elif status == "partial":
            self.color = "#ffa500"
        else:
            self.color = "#ff0000"


    ## Changes status
    def changeStatus(self,status):
        self.status = status

        
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
        text_rect.center = self.rect.center ## Center text in the box

        ## Draw text & box
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(textSurface,textRect)


    ## Updates letter
    def writeLetter(self,letter):
        self.letter = letter

