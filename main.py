import pygame, random
import box_class

############# GAME SETUP #################
 
## Initialize program
pygame.init()
 
## create screen
screen = pygame.display.set_mode((400,600))

## title
pygame.display.set_caption("Wordle")


######### CREATING BASIC VARIABLES ########

## generate a random word
word = random.choice(["hello","great","santa"])

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
guessed = False

## holds indexes for guesses variable
currentWord = 0
currentLetter = 0
