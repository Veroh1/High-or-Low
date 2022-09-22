#Imports
from random import randint
from replit import clear
from art import logo

#Functions
def check_answer(pick, num, turns):
    """Checks the relationship between the two numbers and returns a string telling player that their number is too high or low."""
    if pick > num:
        print("Too high")
        return turns - 1
    elif pick < num:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {num}")
    
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def number_guess():
    #Greet user
    print("Welcome to High or Low!")
    print("I'm thinking of a number between 1 and 100.")
    #Init var
    pick = 0
    num = randint(1,101)
    turns = set_difficulty()
    #Debugging code
    #print(f"Pssst, the correct answer is {num}") 

    #main game logic
    while pick != num:
        print(f"You have {turns} guesses remaining.")
        pick = int(input("Make a guess: "))
        
        turns = check_answer(pick, num, turns)
        if turns == 0:
          print("You've run out of guesses, you lose.")
          return
        elif pick != num:
          print("Guess again.")
            

#Global Variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Active Code

while input("Do you want to play a game? Type 'y' or 'n':\n").lower() == "y":
    clear()
    print(logo)
    number_guess()
