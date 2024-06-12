import random 

def check_guess(guess):
    if guess.lower() in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")


def ask_for_input():
    while True:
        guess = input("Guess a letter!: ")
        if guess.isalpha() and len(guess) == 1:
            print(f"Good guess!")
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")   
    return guess      


word_list = ["pineapple", "mango", "blueberry", "watermelon", "banana"]
word = random.choice(word_list)   


#guess = ask_for_input()

check_guess("b")

#while True:
#    guess = input("Guess a letter!: ")
#    if guess.isalpha() and len(guess) == 1:
#        if guess in word:
#            print(f"Good guess! {guess} is in the word.")
#            break
#        else:
#            print(f"Sorry, {guess} is not in the word. Try again")
#    else: 
#        print("Invalid letter. Please, enter a single alphabetical character.") 




     

