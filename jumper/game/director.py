
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
        self.word_list = []


    def configure_list(self):
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
            file_path = self.wordlist_generator.GUI_select_file("Select word list")
            list = self.wordlist_generator.import_list(file_path)

        # use default
        else:
            list = self.wordlist_generator.default_list()

        return list


    def start_game(self):

        # pick a word list
        self.configure_list()

    def word(self):
        self.word = Word()



    