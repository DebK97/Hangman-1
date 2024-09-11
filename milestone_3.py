import random


print("Welcome to Hangman!")
print("------------------------------------------")

# Possible word choices 
word_list = ['strawberry', 'apple', 'banana', 'orange', 'pear']
word = random.choice(word_list)

guess = input("Please enter a letter: ")

while len(guess) == 1 and guess.isalpha() :
    break
else :
    print("Invalid letter. Please, enter a single alphabetical character.")

    
