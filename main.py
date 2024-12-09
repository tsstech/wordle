import pygame, random, sys
import box_class, button_class, func, words

############# GAME SETUP #################
 
## Initialize program
pygame.init()
 
## create screen
screen = pygame.display.set_mode((400,600))

## title
pygame.display.set_caption("Wordle")


## play again button
playAgainButton = button_class.Button(100, 530, 200, 55, 40, "Play Again", "#02a102")

gameloop = True

########## GAMELOOP ##########
while gameloop:

    ## generate a random word
    word = random.choice(words.dictionary).upper()

    ## reset guesses grid
    guesses = func.resetGuesses()

    ## holds indexes for guesses variable
    currentWord = 0
    currentLetter = 0

    ## while loop condition variables
    attempts = 0
    win = False

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


    ############# GAME OVER #############
    ## Display win/lose message
        if win:
            func.winMessage(screen)
        else:
            func.loseMessage(screen,word)

    playAgain = False
            

    ######### PLAY AGAIN BUTTON ###########
    while not playAgain:

        for event in pygame.event.get():    ## for every event
            if event.type == pygame.QUIT:   ## if cross is clicked
                sys.exit()                  ## end program

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playAgainButton.isOver(pos):
                    playAgain = True
                    attempts = 0
                    win = False
                    print(playAgain)

        

        playAgainButton.draw(screen) ## play again buttonm

        pygame.display.update()

    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

