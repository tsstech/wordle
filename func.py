import pygame, requests
import box_class


## checks if whole word is correct
def checkIfCorrect(guess,word):
    for ind,letter in enumerate(guess):
        if letter.letter != word[ind]:
            return False
    return True


## checks if word exists in api
def checkWordExists(word):
    response = requests.get(f"https://api.datamuse.com/words?sp={word.lower()}&max=1")    ## make api request
    data = response.json()  ## parse json response

    if data:    ## if response is not empty (meaning word exists)
        return True
    else:
        return False


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


## draws Wordle game title
def drawWordle(screen):
    font = pygame.font.Font(None,80)    ## create font object
    textSurface = font.render(f"Wordle",True,(0,0,0))   ## Render the text
    textRect = textSurface.get_rect()   ## Get rect object for text
    textRect.center = pygame.Rect(0,5,400,90).center ## Center text in the box
    screen.blit(textSurface,textRect)


## generate random word using Data Muse API
def generateWord():
    response = requests.get("https://api.datamuse.com/words?sp=?????&max=1")    ## make api request
    data = response.json()  ## parse json response
    return data[0]["word"]  ## return the word

            
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


