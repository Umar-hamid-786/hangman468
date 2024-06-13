import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess.lower() in self.word:
         print(f"Good guess! {guess} is in the word.")
         for i in range(len(self.word)):
            if self.word[i] == guess and self.word_guessed[i] == "_":
               self.word_guessed[i] = guess
               self.num_letters -= 1             
        else:
         self.num_lives -= 1
         print(f"Sorry, {guess} is not in the word. Try again")
         print("You have {num_lives} lives left.")

    def ask_for_input(self):
       while True:
          guess = input("Guess a letter: ")
          if not guess.isalpha() or len(guess) != 1:
             print("Invalid letter. Please, enter a single alphabetical character.")
          elif guess in self.list_of_guesses:
             print("You already tried that letter!")
          else:
             self.check_guess(guess)
             self.list_of_guesses.append(guess)   
             break
            

word_list = ["pineapple", "mango", "blueberry", "watermelon", "banana"]
game = Hangman(word_list)   

