import pygame

class Key:
    def __init__(self,x,y,width,height,letter):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__rect = pygame.Rect(x,y,width,height)
        self.__letter = letter
        self.__color = "#e8e8e8"
        

    ## Changes color based on status
    def changeColor(self,status):
        if status == "empty":
            self.__color = "#e8e8e8"
        elif status == "correct":
            self.__color = "#02a102"
        elif status == "partial":
            self.__color = "#ffa500"
        else:
            self.__color = "#575757"


    ## Draws box & letter
    def drawBox(self, screen):
        ## Define the text
        font = pygame.font.Font(None,30)    ## create font object
        textSurface = font.render(self.__letter,True,(255,255,255))   ## Render the text
        textRect = textSurface.get_rect()   ## Get rect object for text
        textRect.center = self.__rect.center ## Center text in the box

        ## Draw text & box
        pygame.draw.rect(screen, self.__color, self.__rect)
        screen.blit(textSurface,textRect)


    ## Getter method for letter attribute
    def getLetter(self):
        return self.__letter
        
