import random

# List of words to choose from
words = ['python', 'java', 'ruby', 'javascript', 'hangman', 'programming', 'developer']

def get_random_word(word_list):
    """Returns a random word from the passed list of strings."""
    return random.choice(word_list)

def display_board(missed_letters, correct_letters, secret_word):
    """Displays the current state of the game board."""
    print("Missed letters:", ' '.join(missed_letters))

    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    print("Current word:", ' '.join(blanks))
    print()

def get_guess(already_guessed):
    """Returns the letter the player entered."""
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        else:
            return guess

def play_hangman():
    """Main function to play Hangman."""
    print('Welcome to Hangman!')
    secret_word = get_random_word(words)
    missed_letters = ''
    correct_letters = ''
    max_attempts = 6

    while True:
        display_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess
            # Check if the player has won
            if all(letter in correct_letters for letter in secret_word):
                print('Congratulations! You have guessed the word:', secret_word)
                break
        else:
            missed_letters += guess
            # Check if the player has lost
            if len(missed_letters) == max_attempts:
                print('You have run out of guesses! The word was:', secret_word)
                break

if __name__ == '__main__':
    play_hangman()