import random

def chooseWord():                                   # Return a random word from the list
    wordSelection = ['camel','aadvark','ghost']
    secretWord = random.choice(wordSelection)
    return(secretWord)

def userGuessed(guess,secretWord,guessedWord):      # Checks if a guessed letter is in the secret word. If it is, it updates the guessedWord to fill in the blanks of the guessed letter
    if guess in secretWord:
        updatedGuessedWord = revealLetter(guess,secretWord,guessedWord)
        isGoodGuess = True
        return(updatedGuessedWord, isGoodGuess)
    else:
        isGoodGuess = False
        return(guessedWord,isGoodGuess)

def revealLetter(guess,secretWord,guessedWord):     # Fills in the blank of a word based on the guessed letter
    iteration = 0
    for x in secretWord:
        if x == guess:
            guessedWord[iteration] = guess
        iteration += 1
    return(guessedWord)

def  makeGuessedWord(secretWord):               # Make the "blank" version of a word, which is just a list with a number of underscores ("_") the same as the number of letters in the secret word
    guessedWord = []
    for x in secretWord:
        guessedWord.append("_")
    return(guessedWord)

def listToString(userList):                     # Turn a list into a concatonated string
    s = ''
    for x in userList:
        s += x
    return(s)

def checkForWinState(guessedWord):              # Checks if there are any remaining blank characters in the word
    print(guessedWord)
    for x in guessedWord:
        if x == "_":
            return(False)
    return(True)



def main():
    secretWord = chooseWord()
    guessedWord = makeGuessedWord(secretWord)
    strikes = 0
    gameRunning = True
    guessedLetters = []

    while gameRunning == True:
        print(guessedWord)
        print("Pick a letter:")
        print("Number of strikes:", strikes)
        guess = input()
        if guess not in guessedLetters:
            guessedLetters.append(guess)
            guessedLetters = sorted(guessedLetters)
            guessedWord, isGoodGuess = userGuessed(guess,secretWord,guessedWord)
            if isGoodGuess == False:
                strikes += 1
            userWin = checkForWinState(guessedWord)
            if userWin == True:
                print("You won! The word was", secretWord)
                gameRunning = False
            if strikes > 5:
                print("Game over man. You did not get it.")
                print("The secret word was", secretWord)
                gameRunning = False
        else:
            print("You have already guessed that letter! Here are the letters you have already guessed:")
            print(guessedLetters)
            


main()
