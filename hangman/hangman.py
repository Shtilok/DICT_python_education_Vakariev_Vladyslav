import random

def choose_word():
    words = ['python', 'java', 'javascript', 'php']
    return random.choice(words).upper()

def display_word_partial(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "- "
    return display.strip()

def hangman():
    print("HANGMAN")

    secret_word = choose_word()
    guessed_letters = []
    max_attempts = 8

    while max_attempts > 0:
        partial_word = display_word_partial(secret_word, guessed_letters)
        print(f"\n{partial_word}")

        guess = input("Input a letter: > ")

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii() or not guess.islower():
            print("Please enter a single lowercase English letter.")
            continue

        guess = guess.upper()

        if guess in guessed_letters:
            print("You've already guessed this letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            max_attempts -= 1
            print(f"That letter doesn't appear in the word")
        else:
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\nCongratulations! You guessed the word: {secret_word}")
                break
            else:
                print("No improvements")

    if max_attempts == 0:
        print(f"\nYou lost! The correct word was: {secret_word}")

def hangman_menu():
    while True:
        user_choice = input('Type "play" to play the game, "exit" to quit: ')

        if user_choice.lower() == "play":
            hangman()
        elif user_choice.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter either 'play' or 'exit'.")

if __name__ == "__main__":
    hangman_menu()








