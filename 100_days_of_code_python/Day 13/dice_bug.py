from random import randint
dice_img = [1,2,3,4,5,6]
# dice_num = randint(a=1,b=6) -- Will throw an error index out of range  
dice_num = randint(a=0,b=5)
print(dice_img[dice_num])
