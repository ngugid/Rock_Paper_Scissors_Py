import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

player = input("Enter your pick (rock, paper, scissors): ")

print(f"player: {player}")
print(f"computer: {computer}")


if player == computer :
    print("It is a tie!")

elif player == "paper" and computer == "rock":
    print("You Win!")

elif player == "rock" and computer == "scissors":
    print("You Win!")

elif player == "scissors" and computer == "paper":
    print("You Win!")

else: 
    print("You lose!")
print(type(options))