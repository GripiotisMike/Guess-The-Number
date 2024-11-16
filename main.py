import random

# ASCII logo for the game
logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\|  |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
'''

# Main game function
def game():
    print(logo)
    print("Welcome to the Numbers Guessing Game!!! \nI'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    bingo = random.randint(1, 100)
    
    # Ask the user to choose a difficulty
    difficulty = input("Choose a difficulty. Type 'easy'(10 lives) or 'hard'(5 lives): ")
    
    # Set the number of lives based on the difficulty
    lives = 10 if difficulty == "easy" else 5

    # Game loop - player has to guess the number
    while lives > 0:
        print(f"You have {lives} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        
        # Check the player's guess
        if guess == bingo:
            print(f"You got it! The answer was {bingo}.")
            break
        elif guess < bingo:
            print("Too low.")
            lives -= 1
        else:
            print("Too high.")
            lives -= 1

    # If the player runs out of lives, they lose
    if lives == 0:
        print(f"You have run out of guesses, you lose. The correct number was {bingo}.")

# Start the game
game()
