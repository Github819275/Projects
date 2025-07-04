# Hangman game


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    answer = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            answer = answer + secretWord[i] + ' '
        else:
            answer = answer + '_' + ' '
    answer.strip()
    return answer



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    fullString = string.ascii_lowercase
    answer = ''
    for i in range(len(fullString)):
        if fullString[i] not in lettersGuessed:
            answer = answer + fullString[i]
    
    return answer
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    
    guessed = False
    attemptsRemaining = 8
    chosenLetters = []
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")
    while not guessed and attemptsRemaining > 0:
        print("You have", attemptsRemaining, "guesses left.")
        availableLetters = getAvailableLetters(chosenLetters)
        print("Available letters:", availableLetters)
        userGuess = input("Please guess a letter: ")
        while userGuess not in availableLetters:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, chosenLetters))
            print("-------------")
            print("You have", attemptsRemaining, "guesses left.")
            availableLetters = getAvailableLetters(chosenLetters)
            print("Available letters:", availableLetters)
            userGuess = input("Please guess a letter: ")
            
        
        if userGuess in secretWord:
            chosenLetters.append(userGuess)
            chosenLetters.sort()
            print("Good guess:", getGuessedWord(secretWord, chosenLetters))
            
        else:
            chosenLetters.append(userGuess)
            chosenLetters.sort()
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, chosenLetters))
            attemptsRemaining -= 1
            
        
        print("-------------")
        
        if isWordGuessed(secretWord, chosenLetters):
            guessed = True
            
    if guessed:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord, end='.')
        
                


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
