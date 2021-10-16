def import_list(path):
    """
    Loads a CSV file and returns a list of words
    PARAMETERS:
        self (WordListGenerator)        : an instance of WordListGenerator
        path (STR)                      :   the path of a file
    RETURNS:
        a lit of words
    """
    list = []
    with open(path) as file:
        for line in file:

            # strip newlines
            line = line.strip("\n")

            # replace spaces with commas
            line = line.replace(" ",",")

            # split words
            words_from_line = line.split(",")
            for word in words_from_line:

                # append individual words to list
                list.append(word)

    return list     



list = import_list("wordlist")

for i in list:
    print(i)