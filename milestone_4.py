import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialize attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def pick_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        # Check if the guess is in the word
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
        
    def ask_for_input(self):
        # Ask the user to guess a letter and check for valid input
        while True:
            guess = input("Guess a letter: ").lower()
            
            # Check if the guess is NOT a single alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

# Usage
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    game = Hangman(words)
    game.ask_for_input()
