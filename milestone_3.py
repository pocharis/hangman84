import random



word_list = ['Mango', 'Orange', 'Apple', 'Banana', 'Watermelon']

def check_guess(guessed_letter):
    word = random.choice(word_list)
    if len(guessed_letter) == 1 and guessed_letter.isalpha():
        if guessed_letter.lower() in word.lower():
            print(f"Good guess! {guessed_letter} is in the word.")
            
        else:
            print(f"Sorry, {guessed_letter} is not in the word. Try again.")

def ask_for_input():
    condition = True
    while condition:
        guess = input('Enter an alphabet: ')
        check_guess(guess)
        condition = False

ask_for_input()