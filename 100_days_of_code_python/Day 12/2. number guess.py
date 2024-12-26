import random

print("Welcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100.")
diff_type = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()

my_num = random.randrange(1,101)

def num_guess(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > my_num:
            print("Too high.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
        elif user_guess < my_num:
            print("Too low.")
            attempts -=1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
        else:
            print(f"You got it! The answer was {my_num}.")
            break

if diff_type == 'easy':
    attempts = 10
    num_guess(attempts)
elif diff_type == 'hard':
    attempts = 5
    num_guess(attempts)
else:
    print("Enter proper value for difficulty type.")
