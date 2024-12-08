import pygame, random, sys
import box_class, func, words

############# GAME SETUP #################
 
## Initialize program
pygame.init()
 
## create screen
screen = pygame.display.set_mode((400,550))

## title
pygame.display.set_caption("Wordle")


######### CREATING BASIC VARIABLES ########

## generate a random word
word = random.choice(words.dictionary).upper()

guesses = [[box_class.Box(55, 100, 50, 50),
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

attempts = 0
win = False

## holds indexes for guesses variable
currentWord = 0
currentLetter = 0



########## GAMELOOP ##########
while not win and attempts < 6:

    #### User controls ####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            ## If a letter is clicked
            if event.unicode in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if currentLetter < 4:
                    guesses[currentWord][currentLetter].writeLetter(event.unicode)
                    currentLetter += 1
                elif currentLetter == 4 and guesses[currentWord][currentLetter].letter == "":
                    guesses[currentWord][currentLetter].writeLetter(event.unicode)
                
            ## If backspace is clicked
            if event.key == pygame.K_BACKSPACE:
                ## if it is first 4 letters
                if currentLetter > 0 and currentLetter < 4:
                    currentLetter -= 1
                    guesses[currentWord][currentLetter].deleteLetter()

                ## if it is last letter
                elif currentLetter == 4:
                    ## if box is empty, move to previous box and empty it
                    if guesses[currentWord][currentLetter].letter == "":
                        currentLetter -= 1
                        guesses[currentWord][currentLetter].deleteLetter()
                    ## if box has a letter, just empty box and stay on box
                    else:
                        guesses[currentWord][currentLetter].deleteLetter()

            if event.key == pygame.K_RETURN:
                guessedWord = guesses[currentWord][0].letter + guesses[currentWord][1].letter + guesses[currentWord][2].letter + guesses[currentWord][3].letter + guesses[currentWord][4].letter
                ## if all letters in word are guessed
                if guessedWord.lower() in words.dictionary:
                    attempts += 1

                    ## check & change status of letters
                    for ind,letter in enumerate(guesses[currentWord]):
                        letter.status = func.checkStatus(ind,letter.letter,word)
                        letter.changeColor()
                        
                    win = func.checkIfCorrect(guesses[currentWord],word)

                    ## resetting index variables
                    currentWord += 1
                    currentLetter = 0
                    
    #### drawing objects onto screen
    screen.fill("#ffffff")
    func.drawWordle(screen)
    func.drawGuesses(screen,guesses)
    pygame.display.update()

if win:
    func.winMessage(screen)
else:
    func.loseMessage(screen,word)

pygame.display.update()




