import random
from console import Console

class Word: 
    """ A class responsible for picking a word from a list
        checking whether guessed letters are contained in that word
        and generating strings to represent the revealed word so far.
    ARGS:
        none
    ATTRIBUTES:
        secret_word (STR)   :   the word to be guessed
        word_length (INT)   :   the number of letters in the word
        revealed_word (LIST):   a list of strings


    """

    def __init__(self, list_of_words):

        # pick a word from the list
        self.secret_word = list_of_words[random.randint(0, len(list_of_words)-1 )]
        
        # check length
        self.word_length = len(self.secret_word)

        # initialize with blanks
        self.revealed_word = ["_"] * self.word_length
        #self.revealed_word = "_" * self.word_length

    def get_revealed_word(self):
        """Returns a string showing the revealed word
        RETURNS:
            a string
        """
        string = ""
        for item in self.revealed_word:
            string = string + item
        return string
        # rewrote this to return a value
        # instead of printing it in the function itself
        # for better reusability
        # - Nephi

    def check_guess(self, guess):
        """ Checks the guessed letter against the secret word
        and updates self.revealed_word
        ARGS:
            guess: (a single character string)
        """
        if guess in self.secret_word and len(guess) == 1: 
            self.word_length -=1
            counter = 0
            for letter in self.secret_word:
                if letter == guess:
                    self.revealed_word[counter] = letter
                counter+=1
            #return "correct"
            return True

        if guess in self.secret_word and len(guess) != 1:
            # if we want, we can add code that handles the player
            # guessing strings of more than one character in length.
            # for now, penalize it
            return False

        else:
            #return "incorrect"
            return False

        # rewrote this to return Boolean instead of string to avoid errors
        

# For testing purposes:
def main():
    
    word = Word(["cat", "apple"])
    
    # give it an instance of Console as an attribute for this test function only
    word.console = Console()

    # while word is not fully revealed
    while not word.secret_word == word.get_revealed_word():

        letter = input("enter a letter: ")
        has_letter = word.check_guess(letter)
        if has_letter:
            word.console.display_output("Nice!")
        else:
            word.console.display_output("Nope!")

        word.console.display_output()
        # display revealed word so far
        revealed_word_so_far = word.get_revealed_word()

        word.console.display_output(revealed_word_so_far)

        continue
    
    # Word is fully revealed:
    word.console.display_output("The word is fully revealed.")
    word.console.display_output("Good job!")

if __name__ == "__main__":
    main()

