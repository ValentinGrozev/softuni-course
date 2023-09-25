import random

from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

computer_move = ""
player_score = 0
computer_score = 0

player_move = input("Choose [r] for Rock, [p] for Paper, [s] for Scissors: ")

if player_move == "r" or "R":
    player_move = rock
elif player_move == "p" or "P":
    player_move = paper
elif player_move == "s" or "S":
    player_move = scissors
else:
    raise SystemExit("Invalid input, Try again...")

computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")
if player_move == rock and computer_move == scissors or \
        player_move == paper and computer_move == rock or \
        player_move == scissors and computer_move == paper:
    player_score += 1
    print(Fore.GREEN + "You win!")
elif player_move == computer_move:
    print(Fore.BLUE + "Draw!")
else:
    computer_score += 1
    print(Fore.RED + "You lose!")

print(f"Player Score {player_score}:{computer_score} Computer Score ")

player_decision = input("Type [yes] to play again or [no] to quit: ")

while player_decision == "yes" or player_decision == "Yes":
    player_move = input("Choose [r] for Rock, [p] for Paper, [s] for Scissors: ")

    if player_move == "r" or "R":
        player_move = rock
    elif player_move == "p" or "P":
        player_move = paper
    elif player_move == "s" or "S":
        player_move = scissors
    else:
        raise SystemExit("Invalid input, Try again...")

    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")
    if player_move == rock and computer_move == scissors or \
            player_move == paper and computer_move == rock or \
            player_move == scissors and computer_move == paper:
        player_score += 1
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        print(Fore.BLUE + "Draw!")
    else:
        computer_score += 1
        print(Fore.RED + "You lose!")

    print(f"Player Score {player_score}:{computer_score} Computer Score ")
    player_decision = input("Type [yes] to play again or [no] to quit: ")

else:
    print(f"Player Score {player_score}:{computer_score} Computer Score ")
    print("Thank you for playing")