import random

player = ["Rock", "Paper", "Scissors"]
computer = ["Rock", "Paper", "Scissors"]
length = len(computer) - 1
index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computerIndex = random.randint(0, length)
print(f"Computer chose {computer[computerIndex]}")

if index == computerIndex:
  print("It's a tie!")

elif player[index] == "Paper":
  if computer[computerIndex] == "Rock":
    print("You win!")
  else:
    print("You lose!")

elif player[index] == "Rock":
  if computer[computerIndex] == "Scissors":
    print("You win!")
  else:
    print("You lose!")
  
elif player[index] == "Scissors":
  if computer[computerIndex] == "Paper":
    print("You win!")




