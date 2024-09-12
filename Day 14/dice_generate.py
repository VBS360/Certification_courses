import random

dice_num_1 = [1,2,3,4,5,6]
dice_num_2 = [1,2,3,4,5,6]

rand_num_1 = random.randint(0,5)
rand_num_2 = random.randint(0,5)
rand_digit_1 = dice_num_1[rand_num_1]
rand_digit_2 = dice_num_2[rand_num_2]


print(f"First Dice: {rand_digit_1}, Second Dice: {rand_digit_2}")
