# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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
    
    for i in range(len(secretWord)):
        if lettersGuessed.count(secretWord[i]) == 0:
            return False
    return True

'''secretWord = 'apple'
lettersGuessed1 = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed1))
lettersGuessed2 = ['e', 'l', 'k', 'p', 'r', 'a']
print(isWordGuessed(secretWord, lettersGuessed2))
'''
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    GuessedWord = ''
    for i in range(len(secretWord)):
        if lettersGuessed.count(secretWord[i]) == 0:
            GuessedWord += '_ '
        else:
            GuessedWord += secretWord[i]

    return GuessedWord
'''    
print(getGuessedWord(secretWord, lettersGuessed1))
print(getGuessedWord(secretWord, lettersGuessed2))
'''
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    AvailableLetters = ''
    for a_letter in string.ascii_lowercase[::]:
        if lettersGuessed.count(a_letter) == 0:
            AvailableLetters += a_letter
    return AvailableLetters

#print(getAvailableLetters(lettersGuessed1))    


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
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is',len(secretWord), 'letters long.')
#    print ('-------------')
    cycle_Guess = 8
    lettersGuessed = []
    for cycle in range (cycle_Guess):
        print ('-------------')

        print ('You have',cycle_Guess-cycle,'guesses left.')
        AvailableLetters = getAvailableLetters(lettersGuessed)

        print('Available letters:',AvailableLetters)

        while True:
            guess_a_letter = input ('Please guess a letter:')
            guess_a_letter = guess_a_letter.lower()
            if AvailableLetters.count(guess_a_letter) > 0:
                break
            print ('Oops! You have already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
            print ('-------------')
            print ('You have ',cycle_Guess-cycle,'guesses left.')
            print('Available letters: ',AvailableLetters)

        lettersGuessed.append(guess_a_letter)
        if secretWord.count(guess_a_letter) == 0:
            print ('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))

        else:
            print ('Good guess: ',getGuessedWord(secretWord, lettersGuessed))
            
            if isWordGuessed(secretWord, lettersGuessed):
                print ('-------------')

                print ('Congratulations, you won!')
                return

    print ('Sorry, you ran out of guesses. The word was',secretWord,'.')
    return

            

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
