import random
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

comp_num = random.randrange(0,101)
attempt_easy = 10
attempt_hard = 5

if difficulty_level == "easy":
    for attempts in range(0,attempt_easy):
        user_guess = int(input("Make a guess: "))
        if attempt_easy > 0:
            if user_guess > comp_num:
                print("Too high. Guess again.")
                attempt_easy -=  1
            elif user_guess < comp_num:
                print("Too low. Guess again.")
                attempt_easy -=  1
            elif user_guess == comp_num:
                print(f"You got it! The answer was {comp_num}.")
                break
            else:
                pass
        else:
            print("You've run out of guesses, you lose.")
            break
        print(f"You have {attempt_easy} attempts remaining to guess the number.")
elif difficulty_level == "hard":
        for attempts in range(0,attempt_hard):
            user_guess = int(input("Make a guess: "))
            if attempt_easy > 0:
                if user_guess > comp_num:
                    print("Too high. Guess again.")
                    attempt_hard -=  1
                elif user_guess < comp_num:
                    print("Too low. Guess again.")
                    attempt_hard -=  1
                elif user_guess == comp_num:
                    print(f"You got it! The answer was {comp_num}.")
                    break
                else:
                    print("enter proper value.")
            else:
                print("You've run out of guesses, you lose.")
                break
            print(f"You have {attempt_hard} attempts remaining to guess the number.")
else:   
    print("Enter proper value from easy or hard.")
