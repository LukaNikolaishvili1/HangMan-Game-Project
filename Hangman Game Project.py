import random

def select_word():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
        if len(words) == 0:
            raise ValueError("The word list is empty.")
        return random.choice(words)
    except FileNotFoundError:
        print("Missing 'words.txt'. Exiting game.")
        exit()
    except Exception as e:
        print(f"Error occurred: {e}")
        exit()

def display_word(word, guessed_letters):
    result = []
    for char in word:
        if char in guessed_letters:
            result.append(char)
        else:
            result.append('_')
    return ''.join(result)

def display_attempts(remaining_attempts, incorrect_guesses):
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print(f"Remaining attempts: {remaining_attempts}")

def get_user_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").upper()
        if len(guess) != 1:
            print("Please enter a valid letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter!")
        else:
            return guess

def update_game_state(word, guess, guessed_letters, incorrect_guesses, remaining_attempts):
    guessed_letters.append(guess)
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        incorrect_guesses.append(guess)
        remaining_attempts -= 1
        print(f"Sorry, {guess} is not in the word.")
    return guessed_letters, incorrect_guesses, remaining_attempts

def check_win(word, guessed_letters):
    return all(char in guessed_letters for char in word)

def check_game_over(remaining_attempts):
    return remaining_attempts <= 0

def main():
    word = select_word()
    guessed_letters = []
    incorrect_guesses = []
    remaining_attempts = 6
    game_over = False

    print("Welcome to Hangman!")
    print("Try to guess the word!")

    while not game_over:
        print("\nCurrent word: " + display_word(word, guessed_letters))
        display_attempts(remaining_attempts, incorrect_guesses)

        guess = get_user_guess(guessed_letters)
        guessed_letters, incorrect_guesses, remaining_attempts = update_game_state(word, guess, guessed_letters,
                                                                                   incorrect_guesses,
                                                                                   remaining_attempts)

        if check_win(word, guessed_letters):
            print(f"\nCongratulations! You've guessed the word: {word}")
            game_over = True
        elif check_game_over(remaining_attempts):
            print(f"\nGame Over! The word was: {word}")
            game_over = True

    play_again = input("Do you want to play again? (y/n): ").lower()
    while play_again != "y" or "n":
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y" or 'Y':
            main()




if __name__ == "__main__":
    main()
