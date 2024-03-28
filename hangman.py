import random
import getpass

listOfWords = ["multumesc", "capac", "galeata", "unt", "video"]
wordToGuess = ""
word = ""
countWrong = 0

def chooseGameType():
    playerChoice = input("Type 1 for single player and 2 for multiple players: ")

    global wordToGuess
    global word

    if int(playerChoice) == 1:
        wordToGuess = random.choice(listOfWords) 
    else: 
        wordToGuess = getpass.getpass("Type a word: ")

    dashes = len(wordToGuess)
    word = "_" * dashes
    print(word)

    while countWrong < 10 and "_" in word:
        hangman()

    if countWrong >= 10:
        print("You lost")
    else:
        print("Bravo")

def hangman():
    global wordToGuess
    wordToGuessList = list(wordToGuess)
    global word
    wordList = list(word)
    inputLetter = input("Enter a letter: ")
    print("You entered: ", inputLetter)
    if inputLetter in wordToGuessList:
        for i in range(len(wordToGuessList)):
            if wordToGuessList[i] == inputLetter:
                wordList[i] = inputLetter

        word = ''.join(wordList)
        print(word)
    else:
        global countWrong
        countWrong += 1
        print("You have " + str(10 - countWrong) + " chances left")

chooseGameType()