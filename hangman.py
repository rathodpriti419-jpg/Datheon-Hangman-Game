```python
import random

# Words used in the game
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "software",
    "technology",
    "hangman",
    "education"
]

# Hangman drawing stages
hangman_stages = [
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


def play_hangman():
    # Select a random word
    secret_word = random.choice(words).upper()

    # Store guessed letters
    guessed_letters = set()

    # Count incorrect guesses
    wrong_guesses = 0
    max_attempts = 6

    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME")
    print("=" * 40)
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses available.")

    while wrong_guesses < max_attempts:

        # Display hangman drawing
        print(hangman_stages[wrong_guesses])

        # Display the word with hidden letters
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", display_word)

        # Display guessed letters
        if guessed_letters:
            print(
                "Guessed letters:",
                " ".join(sorted(guessed_letters))
            )
        else:
            print("Guessed letters: None")

        print("Attempts remaining:", max_attempts - wrong_guesses)

        # Check whether the word is completely guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The word was:", secret_word)
            return

        # Get user input
        guess = input("\nEnter one letter: ").strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter one letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed this letter. Try another.")
            continue

        # Save the guessed letter
        guessed_letters.add(guess)

        # Check the guessed letter
        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    # Display final drawing
    print(hangman_stages[wrong_guesses])
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)


# Start the game
if __name__ == "__main__":
    play_hangman()