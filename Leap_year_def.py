import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

your_choice = []
computer_choice = []
your_choice = random.choices(cards,k=2)
computer_choice = random.choices(cards,k=2)

for card in your_choice:
    sum_your_choice = 0
    sum_your_choice += your_choice[range(your_choice-1)]