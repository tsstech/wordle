import pygame

class Box:
    def __init__(self,x,y,width,height):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__rect = pygame.Rect(x,y,width,height)
        self.__letter = ""
        self.__color = "#e8e8e8"
        self.__status = "empty"


    ## Changes color based on status
    def changeColor(self):
        if self.__status == "empty":
            self.__color = "#e8e8e8"
        elif self.__status == "correct":
            self.__color = "#02a102"
        elif self.__status == "partial":
            self.__color = "#ffa500"
        else:
            self.__color = "#575757"

    ## checks status of guessed letters in word
    def changeStatus(self,ind,word):
        if self.__letter == word[ind]:
            self.__status = "correct"
        elif self.__letter in word:
            self.__status = "partial"
        else:
            self.__status = "wrong"

        
    ## Deletes letter
    def deleteLetter(self):
        self.__letter = ""
        self.__status = "empty"


    def getLetter(self):
        return self.__letter

    
    def getStatus(self):
        return self.__status


    ## Draws box & letter
    def drawBox(self, screen):
        ## Define the text
        font = pygame.font.Font(None,36)    ## create font object
        textSurface = font.render(self.__letter,True,(255,255,255))   ## Render the text
        textRect = textSurface.get_rect()   ## Get rect object for text
        textRect.center = self.__rect.center ## Center text in the box

        ## Draw text & box
        pygame.draw.rect(screen, self.__color, self.__rect)
        screen.blit(textSurface,textRect)


    ## Updates letter
    def writeLetter(self,letter):
        self.__letter = letter.upper()

