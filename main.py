logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\|  |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  '''

import random


def game():
    print(logo)
    print("Welcome to the Numbers Guessing Game!!! \nI'm thinking of a number between 1 and 100.")
    bingo = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy'(10 lives) or 'hard'(5 lives): ")
    lives = 0
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    while lives > 0:
        print(f"You have {lives} attempts to guess the number.")
        guess = int(input("Make a guess:"))
        if guess == bingo:
            print(f"You got it! the answer was {bingo}.")
        elif guess < bingo:
            print("Too low.")
            lives -= 1
        else:
            print("Too High")
            lives -= 1
    print("You have run out of guesses, you loose.")


game()
