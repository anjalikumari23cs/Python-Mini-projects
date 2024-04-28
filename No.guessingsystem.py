import random
def play_game():
    attempts_left = 5
    random_number = random.randint(1, 20)
    print("I have randomly chosen a number between 1 and 20.")
    while attempts_left > 0:
        user_guess = int(input("Guess the number: "))
        if user_guess == random_number:
            print("Congratulations! You guessed the right number.")
            break
        elif user_guess < random_number:
            print("Try again! You guessed too small.")
        else:
            print("Try again! You guessed too high.")
        attempts_left -= 1
    if attempts_left == 0:
        print(f"Out of attempts! The correct number was {random_number}.")
play_game()