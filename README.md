# Mastermind
This Python implementation of the classic Mastermind game challenges players
to guess a secret code composed of four colors within a limited number of attempts. 

## Game Rules
Objective: Guess the correct sequence of four colors (the "code") in the correct positions.

Color Choices: The valid colors for the code are:

R (Red)
G (Green)
B (Blue)
Y (Yellow)
W (White)
O (Orange)
Code Length: The secret code consists of 4 color slots, and the same color may appear more than once.

Feedback: After each guess, the game will provide:

Correct Positions: Number of colors that are both in the correct position and are the correct color.
Incorrect Positions: Number of colors that are correct but in the wrong position.
Winning: The player wins if they guess the exact code (all colors in the correct positions) within 10 tries. If the player doesn't guess the correct code after 10 tries, the game will reveal the code.

## Files and Functions:
generate_code():
Generates the secret code by selecting four random colors from the available set (R, G, B, Y, W, O).

guess_code():
Prompts the player to enter a guess. It ensures that the input contains four valid colors and rejects any invalid inputs.

check_code(guess, real_code):
Compares the player's guess with the secret code. It returns two values:

correct_pos: Number of correct colors in the correct positions.
incorrect_pos: Number of correct colors in the wrong positions.
game():
The main game loop. It sets up the game, tracks the number of attempts, and checks the player’s guesses against the secret code. It provides feedback after each guess and ends the game after either a win or a loss.
