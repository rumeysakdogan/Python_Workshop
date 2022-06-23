import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0,2)

if user == 0:
  print(rock)
elif user == 1:
  print(paper)
else:
  print(scissors)

print("Computer chose:\n")
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
else:
  print(scissors)

if user == computer:
  print("It's a draw")
elif user == 0:
  if computer == 1:
     print("You lose")
  else:
     print("You win!")
elif user == 1:
  if computer == 2:
     print("You lose")
  else:
     print("You win!") 
else:
  if computer == 0:
     print("You lose")
  else:
     print("You win!") 
  