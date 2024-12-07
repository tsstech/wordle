import pygame
import box_class

## draws grid of word guesses
def drawGuesses(screen,guesses):
    for word in guesses:
        for letter in word:
            letter.drawBox(screen)

## checks status of guessed letters in word
def checkStatus(ind,letter,word):
    if letter == word[ind]:
        return "correct"
    elif letter in word:
        return "partial"
    else:
        return "wrong"

## checks if whole word is correct
def checkIfCorrect(guess,word):
    for ind,letter in enumerate(guess):
        if letter != word[ind]:
            return False
    return True
