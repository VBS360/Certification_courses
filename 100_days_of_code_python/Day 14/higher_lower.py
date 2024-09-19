import random

print("Welcome to the higher lower game.")
print("""What gets Googled more?
A frustratingly addictive game of higher or lower using Google searches.

The data is based on global monthly searches in 2017.""")

question_bank = ["Real Madrid CF, a Football club, from Spain.","Cardi B, a Musician, from United States","Nicki Minaj, a Musician, from Trinidad and Tobago.","Justin Timberlake, a Musician and actor, from United States.","Victoria's Secret, a Lingerie brand, from United States.","Emma Watson, a Actress, from United Kingdom.","Katy Perry, a Musician, from United States.","Billie Eilish, a Musician, from United States.","Ronaldinho, a Footballer, from Brasil.","Shakira, a Musician, from Colombia.","Beyoncé, a Musician, from United States.","Justin Bieber, a Musician, from Canada.","UEFA Champions League, a Club football competition, from Europe.","Nike, a Sportswear multinational, from United States.","Kourtney Kardashian, a Reality TV personality, from United States.","Chris Brown, a Musician, from United States.","Dwayne Johnson, a Actor and professional wrestler, from United States.","Miley Cyrus, a Musician and actress, from United States.","Shawn Mendes, a Musician, from Canada.","Kim Kardashian, a Reality TV personality and businesswoman, from United States.","Virat Kohli, a Cricketer, from India.","Gigi Hadid, a Model, from United States.","Cristiano Ronaldo, a Footballer, from Portugal."]

def selection():
    global random_number_1, random_number_2, question_a, question_b
    random_number_1 = random.randint(0, len(question_bank) - 1)
    random_number_2 = random.randint(0, len(question_bank) - 1)
    while random_number_1 == random_number_2:  # To ensure different selections
        random_number_2 = random.randint(0, len(question_bank) - 1)
    question_a = question_bank[random_number_1]
    question_b = question_bank[random_number_2]

def user_point():
    selection()
    print(f"Compare A: {question_a}")
    print(f"Compare B: {question_b}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    global final_score
    if user_choice == "A" and random_number_1 > random_number_2:
        final_score +=1
        user_choice = True
        print(f"You're right! Current score: {final_score}.")
        return user_point()
    elif user_choice == "A" and random_number_1 < random_number_2:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        user_choice = False
        return
    elif user_choice == "B" and random_number_1 < random_number_2:
        final_score +=1
        user_choice = True
        print(f"You're right! Current score: {final_score}.")
        return user_point()
    elif user_choice == "B" and random_number_1 > random_number_2:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        user_choice = False
        return
    else:
        print("Enter Proper value A or B")
        return

final_score = 0
user_choice = True

user_point()