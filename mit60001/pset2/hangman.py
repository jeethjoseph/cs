# Problem Set 2, hangman.py
# Name: Jeeth Joseph 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def test_is_word_guessed():
    print('Testing funtion "is_word_guessed"')
    print('Trying word "apple" with strings "e,i,k,p,r,s"')
    secret_word = 'apple'
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(is_word_guessed(secret_word, letters_guessed))
    print('Trying word "apple" with strings "a,l,e,i,k,p,r,s"')
    secret_word = 'apple'
    letters_guessed = ['a','l','e', 'i', 'k', 'p', 'r', 's']
    print(is_word_guessed(secret_word, letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word =  guessed_word + letter
        else:
            guessed_word = guessed_word + '_ '
    return guessed_word


def test_get_guessed_word():
    print('Testing funtion "get_guessed_word"')
    print('Trying word "apple" with strings "e,i,k,p,r,s"')
    secret_word = 'apple'
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(get_guessed_word(secret_word, letters_guessed))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""   
    for character in string.ascii_lowercase:
       if character not in letters_guessed:
           available_letters = available_letters + character

    return available_letters

    
def test_get_available_letters():
    print('Testing funtion "get_available_letters"')
    print('Trying  strings "e,i,k,p,r,s"')
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(get_available_letters(letters_guessed))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    print("Welcome to the game Hangman")
    print("I'm thinking of a word that is", len(secret_word),"long")
    letters_guessed = []
    while guesses_left > 0:
        print(secret_word)
        print(letters_guessed)
        print("You have", guesses_left, "guesses left")
        print("Available letters are", get_available_letters(letters_guessed))
        guessed_letter = input("Please input a letter:")
        # handling input as alpha
        if guessed_letter.isalpha() == True:
            guessed_letter_lower = guessed_letter.lower()
            if guessed_letter_lower in letters_guessed:
                if warnings_left > 0:
                    print("You have already guessed that letter. This is a warning.You have", warnings_left,"warnings left")
                    warnings_left = warnings_left - 1
                else:
                    print("You have already guessed that letter and you are out of warnings. So you lose a guess. You have",guesses_left, "guesses left")
            else:
                letters_guessed.append(guessed_letter_lower)
                if guessed_letter in secret_word:
                    print("Awesome. Good Guess")
                    print(get_guessed_word(secret_word, letters_guessed))
                    if is_word_guessed(secret_word,letters_guessed) == True:
                        print('Congratulations You win the Game, The secret word is', secret_word)
                        print('Your score is', guesses_left * len(set(secret_word)))
                        break
                else:
                    print("Oops that is not a letter in the Secret Word")
                    guesses_left = guesses_left - 1
        else:
            if warnings_left == 0:
                print("You have used up your warnings,You lose a guess")
                guesses_left = guesses_left - 1
            else:
                warnings_left = warnings_left - 1
                print("Not a valid char!!! Please try again. You have",warnings_left, "warnings left")
    if guesses_left == 0:
        print("You have ran out of guesses. Secret word was",secret_word)



              
    
       
           
   


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    test_word = my_word.replace(" ","")
    if len(test_word) == len(other_word):
        for charindex in range(0,len(test_word)):

            if test_word[charindex] != "_":
                if test_word[charindex] != other_word[charindex]:
                    return False
        return True
    else:
        return False

def test_match_with_gaps():
    print("Testing match_with_gaps")
    print("Testing with te_ t and tact")
    print(match_with_gaps("te_ t", "tact"))
    print("Testing with a_ _ le and apple")
    print(match_with_gaps("a_ _ le", "apple"))







def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""
    for word in wordlist:
        if match_with_gaps(my_word,word) == True:
            possible_matches = possible_matches + word + " "
    if possible_matches == "":
        print("No matches Found")
    else:
        print("Possible word matches are: ")
        print(possible_matches)
    return None

def test_show_possible_matches():
    print("testing show_possible_matches")
    print("testing t_ _ t")
    show_possible_matches("t_ _ t")
    print("Testing aabbbb_ _ f")
    show_possible_matches("aabbbb_ _ f")




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    print("Welcome to the game Hangman")
    print("I'm thinking of a word that is", len(secret_word), "long")
    letters_guessed = []
    while guesses_left > 0:
        print(secret_word)
        print(letters_guessed)
        print("You have", guesses_left, "guesses left")
        print("Available letters are", get_available_letters(letters_guessed))
        guessed_letter = input("Please input a letter:")
        if guessed_letter == '*':
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(guessed_word)
        # handling input as alpha
        elif guessed_letter.isalpha() == True:
            guessed_letter_lower = guessed_letter.lower()
            if guessed_letter_lower in letters_guessed:
                if warnings_left > 0:
                    print("You have already guessed that letter. This is a warning.You have", warnings_left,
                          "warnings left")
                    warnings_left = warnings_left - 1
                else:
                    print(
                        "You have already guessed that letter and you are out of warnings. So you lose a guess. You have",
                        guesses_left, "guesses left")
            else:
                letters_guessed.append(guessed_letter_lower)
                if guessed_letter in secret_word:
                    print("Awesome. Good Guess")
                    print(get_guessed_word(secret_word, letters_guessed))
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print('Congratulations You win the Game, The secret word is', secret_word)
                        print('Your score is', guesses_left * len(set(secret_word)))
                        break
                else:
                    print("Oops that is not a letter in the Secret Word")
                    guesses_left = guesses_left - 1
        else:
            if warnings_left == 0:
                print("You have used up your warnings,You lose a guess")
                guesses_left = guesses_left - 1
            else:
                warnings_left = warnings_left - 1
                print("Not a valid char!!! Please try again. You have", warnings_left, "warnings left")
    if guesses_left == 0:
        print("You have ran out of guesses. Secret word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass
    print("Testing Functions")
    test_is_word_guessed()
    test_get_guessed_word()
    test_get_available_letters()
    test_match_with_gaps()
    test_show_possible_matches()
    print("Testing is done")
    print("-----------------------")
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
