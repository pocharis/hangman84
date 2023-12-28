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
        # Pick a random word from the word_list
        return random.choice(self.word_list)

    def check_guess(self, guess):
        
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            print(self.word_guessed)
            # Replace _ with the guessed letter
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            
            self.num_letters -= 1
        else:
            #  Handle incorrect guesses
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

            

    def ask_for_input(self):
        # Ask the user to guess a letter and check for valid input
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Guess a letter: ").lower()
            
            # Check if the guess is NOT a single alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

        
        if self.num_lives <= 0:
            print("Game over! You ran out of lives.")
        elif self.num_letters == 0:
            print("Congratulations! You guessed the word.")


def play_game(word_list):
    num_lives = 5 
    
    # instance of the Hangman class
    game = Hangman(word_list, num_lives)
    
    while True:  
        if game.num_lives == 0:
            print("You lost!")  
            break
        
        if game.num_letters > 0:
            game.ask_for_input() 
        else:
            print("Congratulations. You won the game!")  
            break

# Usage
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    play_game(words)  