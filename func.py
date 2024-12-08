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
    textRect.center = pygame.Rect(0,470,400,60).center ## Center text in the box
    screen.blit(textSurface,textRect)


## draws winning message
def winMessage(screen):
    font = pygame.font.Font(None,50)    ## create font object
    textSurface = font.render("You Win!",True,(0,0,0))   ## Render the text
    textRect = textSurface.get_rect()   ## Get rect object for text
    textRect.center = pygame.Rect(0,470,400,60).center ## Center text in the box
    screen.blit(textSurface,textRect)


