import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Moves = [Rock, Paper, Scissors]
Your_Move = int(input("Write 0 for Rock, Write 1 for Paper, Write 2 for Scissors \n"))
if Your_Move >= 0 and Your_Move < 3:
   print("Your Move is:")
   print(Moves[Your_Move])
else:
     print("You have entered an invalid Number, You lose")


# if Your_Move == 0:
#     print(f"Your have choosen \n {Rock}")
# elif Your_Move == 1:
#     print(f"Your have choosen \n {Paper}")
# elif Your_Move == 2:
#     print(f"Your have choosen \n {Scissors}")
# else:
#     print("You have entered an invalid Number, You lose")
  
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(Moves[computer_choice])

if Your_Move ==0 and computer_choice ==0:
    print("It's a draw")
elif Your_Move ==1 and computer_choice ==1:
    print("It's a draw")
elif Your_Move ==2 and computer_choice ==2:
    print("It's a draw")
elif Your_Move ==0 and computer_choice ==1:
    print("You Lose")
elif Your_Move ==0 and computer_choice ==2:
    print("You Won")
elif Your_Move ==1 and computer_choice ==0:
    print("You Won")
elif Your_Move ==1 and computer_choice ==2:
    print("You Lose")
elif Your_Move ==2 and computer_choice ==0:
    print("You Lose")
elif Your_Move ==2 and computer_choice ==1:
    print("You Won")
else:
    print("Computer is smarter than you, You loser")