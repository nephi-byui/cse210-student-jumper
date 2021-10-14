
from game.console import Console
from game.wordlist_generator import WordListGenerator
from game.word import Word
#from game.parachute import Parachute

class Director():
    """
    
    ATTRIBUTES:
        word (Word)             :   an instance of Word
        console (Console)       :   an instance of Console
        parachute (Parachute)   :   an instance of Parachute

        keep_playing (BOOL)     :   game will end
    """

    def __init__(self):
        self.keep_playing = True

        self.console = Console()
        self.wordlist_generator = WordListGenerator()
        

        #self.parachute = Parachute()
        #self.word = Word()
        


    def pick_list(self):
        """Asks the user if they want to pick an external word list or use the default
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            a list of words
        """
        while True:
            user_input = self.console.take_input("Would you like to use an external word list? (y/n) ")

            if user_input in ["Y", "y", "N", "n"]:
                break
            else:
                ("Invalid input.")
                continue
        
        # use external
        if user_input in ["Y", "y"]:
            list = self.wordlist_generator.external_list()

        # use default
        else:
            list = self.wordlist_generator.default_list()

        return list


    def start_game(self):

        # pick a word list
        word_list = self.pick_list()

        # game loop
        
        while self.keep_playing:
        
        # start a round
            self.game_over = False
            self.has_won = False
            self.parachute_hp = 5
            self.WordObject = Word(word_list)
            word_length = self.WordObject.word_len

            # pick a word
            self.console.display_output(f"The word is {word_length} letters long.")

            
            while not self.game_over and not self.has_won:
                guess = self.start_turn()
                self.mid_turn(guess)
                self.end_turn()
                continue

            if game_over:
                # game over stuff
                pass
            else:
                # winner stuff
                pass
            # display parachute and word


    def start_turn(self):
        """ The start of a turn
        """
        self.console.display_output(f"PARACHUTE HP: {self.parachute_hp}")
        self.WordObject.print_revealed_word()
        
        guess = self.console.take_input("Enter a letter: ")
        # add code that will only accept one letter
        return guess


    def mid_turn(self, guess):
        """ Calculations once player guesses a letter
        """
        result = self.WordObject.check_guess(guess)
        if result == True:
            pass
        else:
            self.parachute_hp += -1

    def end_turn(self):
        if self.parachute_hp == 0:
            # game over stuff
            self.game_over = True

        elif the_word_is_completely_revealed == True:
        #elif: #the word is completely revealed:
            self.has_won = True

        else:
            pass




    def word(self):
        self.word = Word()