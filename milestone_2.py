import random
word_list = ['Mango', 'Orange', 'Apple', 'Banana', 'Watermelon']

word = random.choice(word_list)

guess = input('Enter a word: ')

if len(guess) == 1 and guess.isalpha():
    print(word, 'Good guess!')
else:
    print("Oops! That is not a valid input.")