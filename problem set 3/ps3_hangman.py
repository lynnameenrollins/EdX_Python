# Hangman game
#

# -----------------------------------
# Helper code

import random

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

# end of helper code
# -----------------------------------

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
    wordGuessed = True;
    for letter in secretWord:
        if letter not in lettersGuessed:
            wordGuessed = False;
        
    return wordGuessed;
'''secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'z', 'l']
print(isWordGuessed(secretWord, lettersGuessed))   
'''

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
 
    dispWord = ""
    for letter in secretWord:
        if letter not in lettersGuessed:
            dispWord = dispWord + " _ ";
        else:
            dispWord = dispWord + letter
    return dispWord;


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    availableLetters = string.ascii_lowercase
    #make a list so it is mutable
    availLetters=[]
    for char in availableLetters[:]:  
        availLetters.append(char)
            
    for letter in lettersGuessed:
            availLetters.remove(letter)
    
    #convert to string
    strAvailLetters=''
    for letter in availLetters:
        strAvailLetters= strAvailLetters + letter
    
    return strAvailLetters;
        
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

    Follows the other limitations detailed in the problem write-up.
    '''

    
    print('Welcome to the game of Hangman!\n')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.\n')
    print('-------------')
    
    noGuessesLeft = 8;
    lettersGuessed = ''
    #print('CHEATER: SECRETWORD ' + secretWord)
    
    while (noGuessesLeft >0 and not isWordGuessed(secretWord, lettersGuessed)):
        print('You have ' + str(noGuessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        
        guess =input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        
        #check to see if letter is already guessed
        if guessInLowerCase in lettersGuessed:
            print('Oops you have already guessed that letter: ')
            print(getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        else: 
            if guessInLowerCase in secretWord:
                print('Good guess!')
            else:
                print('Oops!That letter is not in my word: ')
            lettersGuessed = lettersGuessed + guessInLowerCase
            print(getGuessedWord(secretWord, lettersGuessed))
            noGuessesLeft -=1
            print('-------------')
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The secret word was ' + secretWord)
    
    
    '''
    while()
    guess =input('Please guess a letter: ')
    '''
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
