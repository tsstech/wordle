import pygame
import box_class


## checks if whole word is correct
def checkIfCorrect(guess,word):
    for ind,letter in enumerate(guess):
        if letter.letter != word[ind]:
            return False
    return True


## checks status of guessed letters in word
def checkStatus(ind,letter,word):
    if letter == word[ind]:
        return "correct"
    elif letter in word:
        return "partial"
    else:
        return "wrong"

def resetGuesses():
    return [[box_class.Box(55, 100, 50, 50),
            box_class.Box(115, 100, 50, 50),
            box_class.Box(175, 100, 50, 50),
            box_class.Box(235, 100, 50, 50),
            box_class.Box(295, 100, 50, 50)],

           [box_class.Box(55, 160, 50, 50),
            box_class.Box(115, 160, 50, 50),
            box_class.Box(175, 160, 50, 50),
            box_class.Box(235, 160, 50, 50),
            box_class.Box(295, 160, 50, 50)],
           
           [box_class.Box(55, 220, 50, 50),
            box_class.Box(115, 220, 50, 50),
            box_class.Box(175, 220, 50, 50),
            box_class.Box(235, 220, 50, 50),
            box_class.Box(295, 220, 50, 50)],
           
           [box_class.Box(55, 280, 50, 50),
            box_class.Box(115, 280, 50, 50),
            box_class.Box(175, 280, 50, 50),
            box_class.Box(235, 280, 50, 50),
            box_class.Box(295, 280, 50, 50)],
           
           [box_class.Box(55, 340, 50, 50),
            box_class.Box(115, 340, 50, 50),
            box_class.Box(175, 340, 50, 50),
            box_class.Box(235, 340, 50, 50),
            box_class.Box(295, 340, 50, 50)],
           
           [box_class.Box(55, 400, 50, 50),
            box_class.Box(115, 400, 50, 50),
            box_class.Box(175, 400, 50, 50),
            box_class.Box(235, 400, 50, 50),
            box_class.Box(295, 400, 50, 50)]]


## draws grid of word guesses
def drawGuesses(screen,guesses):
    for word in guesses:
        for letter in word:
            letter.drawBox(screen)


## drawws Wordle game title
def drawWordle(screen):
    font = pygame.font.Font(None,80)    ## create font object
    textSurface = font.render(f"Wordle",True,(0,0,0))   ## Render the text
    textRect = textSurface.get_rect()   ## Get rect object for text
    textRect.center = pygame.Rect(0,5,400,90).center ## Center text in the box
    screen.blit(textSurface,textRect)
            
## draws losing message
def loseMessage(screen,word):
    font = pygame.font.Font(None,50)    ## create font object
    textSurface = font.render(f"The word was {word.lower()}",True,(0,0,0))   ## Render the text
    textRect = textSurface.get_rect()   ## Get rect object for text
    textRect.center = pygame.Rect(0,460,400,60).center ## Center text in the box
    screen.blit(textSurface,textRect)


## draws winning message
def winMessage(screen):
    font = pygame.font.Font(None,50)    ## create font object
    textSurface = font.render("You Win!",True,(0,0,0))   ## Render the text
    textRect = textSurface.get_rect()   ## Get rect object for text
    textRect.center = pygame.Rect(0,460,400,60).center ## Center text in the box
    screen.blit(textSurface,textRect)


