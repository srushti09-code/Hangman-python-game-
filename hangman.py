
import random

words = ["python", "hangman", "computer", "student", "program"]
secret_word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

hangman_art = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

print("================================")
print("     WELCOME TO HANGMAN!")
print("================================")
print("Guess the hidden English word.")
print("You have 6 wrong guesses allowed.")

while wrong_guesses < max_attempts:
    print(hangman_art[wrong_guesses])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in secret_word):
        break

    guess = input("Guess one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
        print("Please enter one English letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if all(letter in guessed_letters for letter in secret_word):
    print("\nCongratulations! You won!")
    print("The word was:", secret_word)
else:
    print(hangman_art[wrong_guesses])
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)

print("Thanks for playing Hangman!")
