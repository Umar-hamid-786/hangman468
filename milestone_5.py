import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''    

    def __init__(self, word_list, num_lives = 5):            #Initialize the attributes as indicated in the docstring
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


    def __check_guess(self, guess):    
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''                                  
        guess = guess.lower()                               #Check if the letter is in the word 
        if guess in self.word:
         print(f"Good guess! {guess} is in the word.")
         for i in range(len(self.word)):
            if self.word[i] == guess and self.word_guessed[i] == "_":
              self.word_guessed[i] = guess
         self.num_letters -= 1             
        else:
         self.num_lives -= 1
         print(f"Sorry, {guess} is not in the word. Try again")
         print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):       
       '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
       '''
                                                                                                    
       while True:                                         #Ask the user for a letter iteratively until the user enters a valid letter
          guess = input("Guess a letter: ")
          if not guess.isalpha() or len(guess) != 1:
             print("Invalid letter. Please, enter a single alphabetical character.")
          elif guess in self.list_of_guesses:
             print("You already tried that letter!")
          else:
             self.__check_guess(guess)
             self.list_of_guesses.append(guess)   
             break
            
def play_game(word_list):                                   #function that starts the game loop and creates an instance called 'game'. 
   num_lives = 5
   game = Hangman(word_list, num_lives)

   while True:
      if game.num_lives == 0:
         print("You lost!")
         break
      elif game.num_letters > 0:
         print("Word to guess:", ' '.join(game.word_guessed))
         game.ask_for_input()
      else:
            print("Congratulations. You won the game!")
            break   


             
word_list = ["pineapple", "mango", "blueberry", "watermelon", "banana"]  # A list of words of my favourite fruits

play_game(word_list)       #Calls the game loop function to start the game, passing the word_list as an argument. 



   