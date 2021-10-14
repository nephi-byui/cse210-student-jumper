import random
#from console import Console

class Word: 
    def __init__(self, list_of_words):
        self.secret_word = list_of_words[random.randint(0, len(list_of_words)-1 )]
        self.word_len = len(self.secret_word)
        self.revealed_word = ["_"] * self.word_len

        #self.console = Console()

    def print_revealed_word(self):
        for item in self.revealed_word:
            # figure out how to port this to console.display_output
            print(item, end="")
        print("\n")

    def check_guess(self, guess):
        if guess in self.secret_word: 
            self.word_len -=1
            counter = 0
            for letter in self.secret_word:
                if letter == guess:
                    self.revealed_word[counter] = letter
                counter+=1
            #return "correct"
            return True
        else:
            #return "incorrect"
            return False

   
def main():
    # For testing purposes:
    word = Word(["cat", "apple"])
    print(word.check_guess("a"))
    word.print_revealed_word()

if __name__ == "__main__":
    main()

