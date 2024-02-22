# Problem Set 4B
# Name: Jeeth Joseph
# Collaborators:
# Time Spent: x:xx

import string


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        # Different way for writing two for loops but make better sematic sense and readability. Is this list
        # enumeration?

        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        upperCase = string.ascii_uppercase
        lowerCase = string.ascii_lowercase
        shift_dict = {}
        for letter in (upperCase + lowerCase):

            if letter in upperCase:
                shifted_index = upperCase.rfind(letter) + shift
                if shifted_index < 26:
                    shift_dict[letter] = upperCase[shifted_index]
                else:
                    shift_dict[letter] = upperCase[shifted_index - 26]  # circular lookup
            else:
                shifted_index = lowerCase.rfind(letter) + shift
                if shifted_index < 26:
                    shift_dict[letter] = lowerCase[shifted_index]
                else:
                    shift_dict[letter] = lowerCase[shifted_index - 26]  # circular lookup
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher_dict = self.build_shift_dict(shift)
        encrypted_message = ''
        for char in self.message_text:
            if char in cipher_dict:
                encrypted_message = encrypted_message + cipher_dict[char]
            else:
                encrypted_message = encrypted_message + char

        return encrypted_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict[:]

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_score = 0
        best_decryption = ''
        best_shift = 0
        for shift in range(27):
            decryption = self.apply_shift(shift)
            score = 0

            for word in decryption.split(' '):
                if is_word(self.valid_words,word):

                    score =  score + 1
            if score > best_score:
                best_score = score
                best_decryption = decryption
                best_shift = shift
        if best_score > 0:
            return (best_shift,best_decryption)
        else:
            raise ValueError("Non decryptable")




if __name__ == '__main__':
    print("----------TESTING BEGIN----------")
    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello world', 2)
    print('Expected Output: jgnnq yqtnf')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('HELLO WORLD!!', 4)
    print('Expected Output: LIPPS ASVPH!!')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    #
    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('LIPPS ASVPH!!')
    print('Expected Output:', (22, 'HELLO WORLD!!'))
    print('Actual Output:', ciphertext.decrypt_message())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('Xoqy Tzcfsm.')
    print('Expected Output:', (12, 'Jack Florey.'))
    print('Actual Output:', ciphertext.decrypt_message())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc')
    print('Expected Output:', (12, 'Jack Florey is a mythical character created on the spur of a moment to'))
    print('Actual Output:', ciphertext.decrypt_message())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh')
    print('Expected Output:', (12, 'Jack Florey is a mythical character created on the spur of a moment'))
    print('Actual Output:', ciphertext.decrypt_message())


    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy.')
    print('Expected Output:', (12, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack.'))
    print('Actual Output:', ciphertext.decrypt_message())

    print("----------TESTING ENDS ALL TESTS CLEAR----------")

    # TODO: best shift value and unencrypted story


    storyCipher = CiphertextMessage(get_story_string())
    print(storyCipher.decrypt_message())

    # Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack.
    # He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the
    # tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming
    # students in the ways, means, and ethics of hacking

