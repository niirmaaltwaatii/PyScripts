import random

# List of words for the Hangman game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the Hangman game
def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while True:
        print("\nWord: " + display_word(word_to_guess, guessed_letters))
        print("Attempts left: " + str(attempts))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            if set(word_to_guess) == set(guessed_letters):
                print("Congratulations! You've guessed the word: " + word_to_guess)
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            if attempts == 0:
                print("Game over! The word was: " + word_to_guess)
                break

if __name__ == "__main__":
    play_hangman()
