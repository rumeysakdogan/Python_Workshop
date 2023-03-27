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

choice_img = [rock, paper, scissors]

# Write your code below this line 👇
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0, 2)

if user >= 3 or user < 0:
    print("Invalid input. You lose!")
else:
    print(choice_img[user])
    print("Computer chose:\n")
    print(choice_img[computer])

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
