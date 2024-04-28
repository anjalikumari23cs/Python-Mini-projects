import random

# Define the possible moves
moves = ["rock", "paper", "scissors"]

# Assign a random play to the computer
computer = random.choice(moves)

# Set player to False
player = False

while not player:
    # Take user input
    user_action = input("Enter a choice (rock, paper, scissors): ")

    # Validate user input
    if user_action.lower() not in moves:
        print("Invalid input. Please choose from 'rock', 'paper', or 'scissors'.")
        continue

    # Determine the winner
    if user_action.lower() == computer:
        print(f"It's a tie! Both players selected {user_action}.")
    elif (user_action.lower() == "rock" and computer == "scissors") or \
         (user_action.lower() == "paper" and computer == "rock") or \
         (user_action.lower() == "scissors" and computer == "paper"):
        print(f"You win! {user_action.capitalize()} beats {computer}.")
    else:
        print(f"You lose! {computer.capitalize()} beats {user_action}.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "no":
        player = True
        print("Thanks for playing!")