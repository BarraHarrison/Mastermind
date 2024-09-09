import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
    return code

def guess_code():
    while True:
        guess = input("Guess (separate colors with space): ").upper().split()

        if len(guess) != CODE_LENGTH:
            print(f"You must guess exactly {CODE_LENGTH} colors.")
            continue

        invalid_colors = [color for color in guess if color not in COLORS]
        if invalid_colors:
            print(f"Invalid colors: {', '.join(invalid_colors)}. Try again.")
            continue

        return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count the colors in the real code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # First pass: Check correct positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # Second pass: Check incorrect positions, but exclude already matched colors
    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind. You have {TRIES} tries to guess the code...")
    print("The valid colors are", " ".join(COLORS))

    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"Congratulations! You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print(f"Sorry, you ran out of tries. The correct code was: {' '.join(code)}")

if __name__ == "__main__":
    game()
