import random

print("Welcome to Hangman!")
print("------------------------------------------")

# Possible word choices 
word_list = ['strawberry', 'apple', 'banana', 'orange', 'pear']
word = random.choice(word_list)

guess = input("Please enter a letter: ")

# making sure "guess" equals to 1 and is alphabetical
if len(guess) == 1 and guess.isalpha() :
  print("Good Guess!")
else :
  print("Oops! That's not a valid input.")  



print(word)
