# A wordle clone
# The user is prompted to guess a word picked from a bank of words. They are provided with data based on the letters they have guessed.
# Users can create their own banks of words with JSON and determine if they want to play in a case sensative fashion.

# Imports
from termcolor import colored as colour, cprint
from random import choice as pick
import json
from time import sleep
import os
from terminalUtils import clear

# Setup Variables
slpMult = 2

guesses = 5

termsize = os.get_terminal_size()[0]

defaultWords = '{ "Case Sensitive" : true , "words" : ["List","Variable","Compile","Memory","Interperator","Algorithm","API","Bug","Conditional","Boolean","Intager","String","Float","Concatinate","Syntax","Bit","Byte","Nibble","Computer","JSON","HTML","CMD"]}'

clear()

# Loads imported file, 
# If there is no file the program will use defualt list, 
# If the file is not in the right format the program will exit.
def loadIFile():
    
    try:    
        iWords = json.load(open('./sadWordle/words.json'))
    except:
        print("No imported word list found! Using default word list \nIf you have tried to import words, make sure they are in the same directory as the python script & ensure that it is called \"words.json\"")
        iWords = json.loads(defaultWords)
        sleep(2*slpMult)
    try:
        caseSensitive = iWords['Case Sensitive']
        words = iWords['words']
    except:
        print("The word import file supplied has not got the right format of data! Refer to the template JSON file.\n\nProgram Exiting in 3 seconds!")
        sleep(3*slpMult)
        exit()
    return(caseSensitive, words)

# Provides instructions
def instructionMenu(): 
    clear()
    print("Welcome to a cmdline wordle")
    print("Its wordle, I'm sure you can figure it out.")
    sleep(2*slpMult)

# Pickes a secret word & tells user if the game will be case sensitive
def setupGame(caseSensitive, words):
    clear()
    if caseSensitive: print("This game will be case sensitive")
    else: print("This game will not be case sensitive")
    sleep(2*slpMult)
    secret = pick(words)

    if not bool(caseSense): secret = secret.lower()

    return secret

# Analyzes a guess based on the secret and returns an array of colours
def analyze(guess,secret):
    retArry = []
    for i in range(len(secret)):
        if guess[i] in secret:
            if guess[i] == secret[i]:
                retArry.append("green")
            else:
                retArry.append("yellow")
        else:
            retArry.append("red")
    return retArry

# The main game loop
def gameLoop(secret,guesses):
    
    # Sets up variables
    guessLimit = guesses
    guessedwords = []
    for i in range(guessLimit): 
        guessedwords.append(" "*len(secret))
            
    letterStatuses = []
    for i in range(guessLimit):
        buffer = []
        for j in secret: buffer.append("white")
        letterStatuses.append(buffer)
    guessNum = 0

    while True:
        clear()
        
        # Displays wordle style grid based on past guesses
        for i in range(guessLimit):
            gWordsBuffer = list(guessedwords[i])
            print(" "*int((termsize/2)-(len(secret)*2)), end="")
            for l in range(len(secret)):
                print(colour("[",letterStatuses[i][l])+colour(gWordsBuffer[l],"white")+colour("]",letterStatuses[i][l]),end=" ")
            print("")
        
        # If the user is out of guesses the game stops
        if guesses == 0: 
            print("YOU LOOSE!".center(termsize))
            print(f"The word was: {secret}".center(termsize))
            break
        
        # Adds space to center the input
        print(" "* int((termsize/2)-(len(secret)*0.5)),end="")

        # Gets user input
        guess = input()
        if len(guess) != len(secret): 
            print(f"That is not the right length word".center(termsize))
            sleep(1)
            continue
        
        # If game is not case sensitive make the guess all lowercase
        if not bool(caseSense): guess = guess.lower()

        # If the user has already guessed the word, prompts the user for a new word
        if guess in guessedwords:
            print(f"You have already guessed {guess}!".center(termsize))
            sleep(1)
            continue

        # If the user has guessed the right word, Win screen, exit game
        if guess == secret:
            print("YOU WIN!".center(termsize))
            if guessNum != 0: plural = "s"
            else: plural = ""
            print(f"You guessed the secret word within {guessNum + 1} attempt{plural}!".center(termsize))
            break

        # Analyze guess and change the colour around the guessed letters
        letterStatuses[guessNum] = analyze(guess,secret)

        # Keeping track of how many turns have occured
        guessedwords[guessNum] = guess
        guessNum += 1
        guesses -= 1
        

# GAME CODE
caseSense,words = loadIFile()
instructionMenu()
gameLoop(setupGame(caseSense,words),guesses)