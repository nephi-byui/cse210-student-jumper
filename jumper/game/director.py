
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
        """
        ARGS:
            self (Director)     : an instance of Director()        
        """
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

    def draw_parachute(self, parachute_hp, safe=False):
        """Draws the state of the parachute
        ARGS:
            self (Director)     : an instance of Director()
            parachute_hp (INT)  : the amount of HP remaining
            safe (BOOL)         : whether or not the game is already won (False by default)
        """
        hits_taken = 4 - parachute_hp
        
        # if game is still ongoing
        if not safe:
            # if alive
            if parachute_hp > 0:
                parachute_ascii = [ "  ___  ",
                                    " /___\ ",
                                    " \   / ",
                                    "  \ /  ",
                                    "   0   ",
                                    "  /|\  ",
                                    "  / \  ",
                                    "       ", 
                                    "^^^^^^^" ]
                
                # replace destroyed lines with empty lines
                for i in range(0, hits_taken):
                    parachute_ascii[i] = "       "

            # if dead
            elif parachute_hp == 0:
                parachute_ascii = [ "       ",
                                    "       ",
                                    "       ",
                                    "       ",
                                    "   X   ",
                                    "  /|\  ",
                                    "  / \  ",
                                    "       ", 
                                    "^^^^^^^" ]

        # game is won
        elif safe:
            parachute_ascii = [ "       ",
                                "       ",
                                " SAFE! ",
                                "       ",
                                "  \o/  ",
                                "   |   ",
                                "  / \  ",
                                "       ", 
                                "^^^^^^^" ]

        # print the output
        for line in parachute_ascii:
            self.console.display_output(line)


    def start_game(self):
        """ The function that is called to start the game
        ARGS:
            self (Director)     : an instance of Director()
        """        

        # pick a word list
        word_list = self.pick_list()
       
        # start a round
        self.game_over = False
        self.has_won = False
        self.parachute_hp = 4

        # create Word()
        self.keep_playing = True
        self.WordObject = Word(word_list)
        word_length = self.WordObject.word_length

        self.console.display_output(f"The word is {word_length} letters long.")
        self.console.display_output()

        # guessing loop
        while True:
            # draw parachute
            
            if self.keep_playing:
                pass
            else:
                # game end code
                break

            # display the revealed word, take player input
            guess = self.start_turn()

            # check guess, update parachute_hp
            # draw parachute 
            self.mid_turn(guess)

            # display stats
            self.status_report()

            # check for game-ending conditions before 
            self.keep_playing = self.is_keep_playing()
            continue            

        if not self.keep_playing and self.parachute_hp == 0:
            # game over stuff
            self.draw_parachute(self.parachute_hp)
            self.console.display_output("You crashed! Game over.")

        elif not self.keep_playing and self.parachute_hp > 0:
            # winner stuff
            self.console.display_output("You reached the ground safely. Good job!")

    def start_turn(self):
        """ The start of a turn
        ARGS:
            self (Director)     : an instance of Director()
        """
        # fetch the word revealed so far
        self.console.display_output(f"{self.WordObject.revealed_word} ({self.WordObject.word_length}-letter word)")
        # display state of parachute
        self.draw_parachute(self.parachute_hp)
        
        # ask for input:
        guess = self.console.take_input("Guess a letter [a-z]: ")
        guess = guess.lower()
        return guess


    def mid_turn(self, guess):
        """ Calculations once player guesses a letter,
        displays letters left, guesses left.
        ARGS:
            self (Director)     : an instance of Director()
            guess (STR)         : a string
        """
        result = self.WordObject.check_guess(guess)
        if result == True:
            self.console.display_output(f"Word contains {guess}!")
        else:
            self.console.display_output(f"Word does not contain {guess}! Ouch!")
            self.parachute_hp += -1

    def status_report(self):
        """ Displays information before starting a new guessing round
            self (Director)     : an instance of Director()
        """
        guesses_left = self.parachute_hp

        if guesses_left == 4:
            hp_report = (f"Your parachute is untouched!")
        elif guesses_left == 3:
            hp_report = (f"No reason to panic. You still have 3 wrong guesses left.")
        elif guesses_left == 2:
            hp_report = (f"You have 2 wrong guesses remaining.")     
        elif guesses_left == 1:
            hp_report = (f"Be careful! One more mistake and you're a goner!")
        elif guesses_left == 0:
            hp_report = (f"Be careful! One more mistake and you're a goner!")

        self.console.display_output(hp_report)
        self.console.display_output()               #newline




    def is_keep_playing(self):
        """ Check for game-ending conditions before starting the next round:
        ARGS:
            self (Director)     : an instance of Director()
        RETURNS:
            a boolean
        """
        # game over (LOSS)
        if self.parachute_hp == 0:
            # game over stuff
            return False
        
        # game over (WIN)
        elif self.WordObject.secret_word == self.WordObject.revealed_word: # the word is completely revealed
            return False

        else:
            # nothing
            return True


# testing
def main():
    from console import Console
    director = Director()
    director.start_game()