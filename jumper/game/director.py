from game.console import Console
from game.wordlist_generator import WordListGenerator
from game.word import Word

class Director():
    """
    
    ATTRIBUTES:
        WordObject (Word)                       : an instance of Word
        wordlist_generator (WordListGenerator)  : an instance of WordListGenerator
        console (Console)                       : an instance of Console

        keep_playing (BOOL)     : end game if False
        parachute_hp (INT)      : HP counter, game over if reaches 0
    """

    def __init__(self):
        """
        ARGS:
            self (Director)     : an instance of Director()        
        """
        
        self.console = Console()
        self.wordlist_generator = WordListGenerator()

        self.keep_playing = True
        self.starting_hp = 4
        self.parachute_hp = self.starting_hp

    
    def pick_list(self):

        """Asks the user if they want to pick an external word list or use the default.
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            a list of words
        """
        is_valid_input = False

        while not is_valid_input:
            user_input = self.console.take_input("Would you like to use an external (CSV) word list? (y/n) ")

            if user_input in ["Y", "y", "N", "n"]:
                is_valid_input = True
                break
            else:
                self.console.display_output("Invalid input.")
                continue
        
       # use external
        if user_input in ["Y", "y"]:
            list = self.wordlist_generator.external_list()
            if list == False:
                list = self.wordlist_generator.default_list()
                self.console.display_output("[ *** ] No external list selected. Using default word list.")
        # use default
        else:
            self.console.display_output("[ *** ] Default word list selected.")
            list = self.wordlist_generator.default_list()

        return list

    def draw_parachute(self, safe=False):
        """Draws the state of the parachute
        ARGS:
            self (Director)     : an instance of Director()
            parachute_hp (INT)  : the amount of HP remaining
            safe (BOOL)         : whether or not the game is already won (False by default)
        """
        parachute_hp = self.parachute_hp
        hits_taken = self.starting_hp - parachute_hp
        
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
                                    " (x_x) ",
                                    f"{self.WordObject.secret_word.upper()}",
                                    "       ",
                                    "   X   ",
                                    "  /|\  ",
                                    "  / \  ",
                                    "       ", 
                                    "^^^^^^^" ]

        # game is won
        elif safe:
            parachute_ascii = [ "       ",
                                " (^_^) ",
                                "YOU WIN",
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

        # create Word()
        self.keep_playing = True
        self.WordObject = Word(word_list)
        word_length = self.WordObject.word_length
        self.already_guessed = [ ]

        self.console.display_output(f"The word is {word_length} letters long.")
        self.console.display_output()

        # guessing loop
        #while True:
        while self.keep_playing:
            # draw parachute
            
            #if self.keep_playing:
            #    pass
            #else:
            #    # game end code
            #    break

            # display the revealed word, take player input
            guess = self.start_turn()

            # check guess, update parachute_hp
            # draw parachute 
            self.mid_turn(guess)

            # display stats
            #self.status_report()

            # check for game-ending conditions before 
            self.keep_playing = self.is_keep_playing()
            continue            

        
        if not self.keep_playing and self.parachute_hp == 0:
            self.game_over()

        elif not self.keep_playing and self.parachute_hp > 0:
            self.victory()

    def status_report(self):
        """ Displays information before starting a new guessing round
            self (Director)     : an instance of Director()
        """
        guesses_left = self.parachute_hp

        if guesses_left > 3:
            hp_report = (f"(^_^) {guesses_left} wrong guesses left.")
        elif guesses_left == 3:
            hp_report = (f"(-_-) 3 wrong guesses left.")
        elif guesses_left == 2:
            hp_report = (f"(o_o) 2 wrong guesses left.")     
        elif guesses_left == 1:
            hp_report = (f"(@_@) Be careful! One more mistake and you're a goner!")
        elif guesses_left == 0:
            hp_report = (f"(x_x) ...")

        self.console.display_output(hp_report)

    def start_turn(self):
        """ The start of a turn.
            Displays the status of the word being guessed,
            the letters that have been uncovered
            takes the input and makes sure it is valid
            and returns that input
        ARGS:
            self (Director)     : an instance of Director()
        RETURNS:
            a string
        """
        # fetch the word revealed so far
        self.console.display_output(f"{self.WordObject.revealed_word} ({self.WordObject.word_length}-letter word)")
        # display state of parachute
        self.draw_parachute()
        
        # displays remaining wrong guesses left
        self.status_report()

        # ask for input:
        is_valid_input = False

        while not is_valid_input:
            guess = self.console.take_input("[ ? ] Guess a letter [a-z]: ")
            guess = guess.lower()

            if len(guess) != 1:
                self.console.display_output(f" !!!  Invalid input. Enter one letter only.")
                continue
            elif guess in self.already_guessed:
                self.console.display_output(f" !!! You already guessed \"{guess},\" try another letter.")
                continue
            else:
                # add the letter to the list
                self.already_guessed.append(guess)
                is_valid_input = True
                break

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
            self.console.display_output(f"(^_^) Word contains \"{guess.upper()}\"")
        else:
            self.console.display_output(f"(T_T) Word does not contain \"{guess.upper()}\"")
            self.parachute_hp += -1
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

    def victory(self):
        self.draw_parachute(safe=True)
        self.console.display_output("(^_^) You reached the ground safely. Good job!")

    def game_over(self):
        self.draw_parachute()
        self.console.display_output(f"(x_x) You crashed! Game over.")
        self.console.display_output(f"The word was: \"{self.WordObject.secret_word.upper()}\"")

# testing
def main():
    from console import Console
    director = Director()
    director.start_game()