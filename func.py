import pygame, requests, random
import box_class, key_class


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

    if data and data[0]["word"].upper() == word:    ## if response is not empty (meaning word exists)
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


## creates new keyboard
def createKeyboard():
    return [[key_class.Key(30, 480, 40, 40, "Q"),
            key_class.Key(80, 480, 40, 40, "W"),
            key_class.Key(130, 480, 40, 40, "E"),
            key_class.Key(180, 480, 40, 40, "R"),
            key_class.Key(230, 480, 40, 40, "T"),            
            key_class.Key(280, 480, 40, 40, "Y"),
            key_class.Key(330, 480, 40, 40, "U"),
            key_class.Key(380, 480, 40, 40, "I"),
            key_class.Key(430, 480, 40, 40, "O"),
            key_class.Key(480, 480, 40, 40, "P")],

            [key_class.Key(60, 530, 40, 40, "A"),
            key_class.Key(110, 530, 40, 40, "S"),
            key_class.Key(160, 530, 40, 40, "D"),
            key_class.Key(210, 530, 40, 40, "F"),
            key_class.Key(260, 530, 40, 40, "G"),            
            key_class.Key(310, 530, 40, 40, "H"),
            key_class.Key(360, 530, 40, 40, "J"),
            key_class.Key(410, 530, 40, 40, "K"),
            key_class.Key(460, 530, 40, 40, "L")],

            [key_class.Key(110, 580, 40, 40, "Z"),
            key_class.Key(160, 580, 40, 40, "X"),
            key_class.Key(210, 580, 40, 40, "C"),
            key_class.Key(260, 580, 40, 40, "V"),
            key_class.Key(310, 580, 40, 40, "B"),            
            key_class.Key(360, 580, 40, 40, "N"),
            key_class.Key(410, 580, 40, 40, "M")]
        ]

## draws keyboard
def drawKeyboard(screen,keyboard):
    for row in keyboard:
        for key in row:
            key.drawBox(screen)


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
    textRect.center = pygame.Rect(0,5,550,90).center ## Center text in the box
    screen.blit(textSurface,textRect)


## generate random word using Data Muse API
def generateWord():
    response = requests.get("https://api.datamuse.com/words?sp=?????&max=1000")    ## make api request
    data = response.json()  ## parse json response
    return random.choice([item['word'] for item in data])  ## return the word

            
## draws losing message
def loseMessage(screen,word):
    font = pygame.font.Font(None,50)    ## create font object
    textSurface = font.render(f"The word was {word.lower()}",True,(0,0,0))   ## Render the text
    textRect = textSurface.get_rect()   ## Get rect object for text
    textRect.center = pygame.Rect(0,460,550,60).center ## Center text in the box
    screen.blit(textSurface,textRect)


## resets wordle grid to empty
def resetGuesses():
    return [[box_class.Box(130, 100, 50, 50),
            box_class.Box(190, 100, 50, 50),
            box_class.Box(250, 100, 50, 50),
            box_class.Box(310, 100, 50, 50),
            box_class.Box(370, 100, 50, 50)],

           [box_class.Box(130, 160, 50, 50),
            box_class.Box(190, 160, 50, 50),
            box_class.Box(250, 160, 50, 50),
            box_class.Box(310, 160, 50, 50),
            box_class.Box(370, 160, 50, 50)],
           
           [box_class.Box(130, 220, 50, 50),
            box_class.Box(190, 220, 50, 50),
            box_class.Box(250, 220, 50, 50),
            box_class.Box(310, 220, 50, 50),
            box_class.Box(370, 220, 50, 50)],
           
           [box_class.Box(130, 280, 50, 50),
            box_class.Box(190, 280, 50, 50),
            box_class.Box(250, 280, 50, 50),
            box_class.Box(310, 280, 50, 50),
            box_class.Box(370, 280, 50, 50)],
           
           [box_class.Box(130, 340, 50, 50),
            box_class.Box(190, 340, 50, 50),
            box_class.Box(250, 340, 50, 50),
            box_class.Box(310, 340, 50, 50),
            box_class.Box(370, 340, 50, 50)],
           
           [box_class.Box(130, 400, 50, 50),
            box_class.Box(190, 400, 50, 50),
            box_class.Box(250, 400, 50, 50),
            box_class.Box(310, 400, 50, 50),
            box_class.Box(370, 400, 50, 50)]]


## draws winning message
def winMessage(screen):
    font = pygame.font.Font(None,50)    ## create font object
    textSurface = font.render("You Win!",True,(0,0,0))   ## Render the text
    textRect = textSurface.get_rect()   ## Get rect object for text
    textRect.center = pygame.Rect(0,460,550,60).center ## Center text in the box
    screen.blit(textSurface,textRect)


