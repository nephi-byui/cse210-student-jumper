# Jumper
Tension so thick you can cut it with a knife! <i>Jumper</i> seems like a pretty 
laid back game until it's not! The rules are simple. The jumper guesses letters, 
one at a time. If the letter's not in the puzzle, the parachute loses a line. 
Guessing continues until the puzzle is solved or, well, you know.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. 
Open a terminal and browse to the project's root folder. Start the program by 
running the following command.
```
python3 jumper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- hunter              (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Tianna DeSpain - des17015@byui.edu
* Nephi Malit - byui@nephi.malit.me
* Tatenda F. Mukaro - muk21002@byui.edu

## Basic Features
---
* The puzzle is a secret word randomly chosen from a list.
* The player guesses a letter in the puzzle.
* If the guess is correct, the letter is revealed.
* If the guess is incorrect, a line is cut on the player's parachute.
* Play continues until the puzzle is solved or the player has no more parachute.

## Extra Features
---
* Option to import a wordlist for an external file
* Displaying the number of wrong guesses remaining
* Enhanced input validation with user-friendly messages and smileys
* Enhanced game play and game over messages