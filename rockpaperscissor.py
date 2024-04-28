import random
moves = ["rock", "paper", "scissors"]
computer = random.choice(moves)
player = False
while not player:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    if user_action.lower() not in moves:
        print("Invalid input. Please choose from 'rock', 'paper', or 'scissors'.")
        continue
    if user_action.lower() == computer:
        print(f"It's a tie! Both players selected {user_action}.")
    elif (user_action.lower() == "rock" and computer == "scissors") or \
         (user_action.lower() == "paper" and computer == "rock") or \
         (user_action.lower() == "scissors" and computer == "paper"):
        print(f"You win! {user_action.capitalize()} beats {computer}.")
    else:
        print(f"You lose! {computer.capitalize()} beats {user_action}.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "no":
        player = True
        print("Thanks for playing!")
