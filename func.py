import pygame
import box_class

def drawGuesses(screen,guesses):
    for word in guesses:
        for letter in word:
            letter.drawBox(screen)
