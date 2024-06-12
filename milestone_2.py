import random

word_list = ["pineapple", "mango", "blueberry", "watermelon", "banana"]

word = random.choice(word_list)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")


print(word_list)

print(word)