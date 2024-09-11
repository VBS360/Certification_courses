import random

# List of card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game_start():
    while True:
        game_start = input(print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
        if game_start == 'y':
            # Randomly select two cards for both the player and the computer
            your_choice = random.choices(cards, k=2)
            computer_choice = random.choices(cards, k=2)
            sum_your_choice = sum(your_choice)
            sum_computer_choice = sum(computer_choice)

            print(f"Your cards: {your_choice}, current_score: {sum_your_choice}")
            print(f"Computer's first card: {computer_choice[0]}")

            # Loop to check if the player wants to add a new card
            while sum_your_choice < 21:
                new_card_select = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                if new_card_select == 'y':
                    new_val = random.choice(cards)  # Choose a single card
                    your_choice.append(new_val)     # Add the new card to the list
                    sum_your_choice = sum(your_choice)  # Recalculate the sum
                    if new_val == 11 and sum_your_choice >= 21:
                        new_val == 1
                        your_choice.pop() 
                        your_choice.append(new_val)     # Add the new card to the list
                        sum_your_choice = sum(your_choice)  # Recalculate the sum
                    print(f"Your cards: {your_choice}, your current_score: {sum_your_choice}")

                    if sum_your_choice >= 21:
                        break

                elif new_card_select == 'n':
                    break

                else:
                    print("Enter proper input value")

                while sum_computer_choice < 16:
                    new_card_computer = random.choice(cards)  # Choose a single card
                    computer_choice.append(new_card_computer)
                    sum_computer_choices = sum(computer_choice)

                    if sum_computer_choices >= 21:
                        break

            # Final output if the loop ends
            if sum_your_choice > 21:
                print(f"""Your final cards: {your_choice}, your final_score : {sum_your_choice}, computer final cards: {computer_choice}, computer score : {sum_computer_choice}
                You went over. You lose 😭""")
            elif sum_computer_choice == 21:
                print(f"""Your final cards: {your_choice}, your final_score : {sum_your_choice}, computer final cards: {computer_choice}, computer score : {sum_computer_choice}
                computer Win with a Blackjack 😤""")
            elif sum_your_choice == 21:
                print(f"""Your final cards: {your_choice}, your final_score : {sum_your_choice}, computer final cards: {computer_choice}, computer score : {sum_computer_choice}
                Win with a Blackjack 😎""")
            elif sum_your_choice > sum_computer_choice:
                print(f"""Your final cards: {your_choice}, your final_score : {sum_your_choice}, computer final cards: {computer_choice}, computer score : {sum_computer_choice}
                "You win 😃""")
            elif sum_computer_choice > sum_your_choice:
                print(f"""Your final cards: {your_choice}, your final_score : {sum_your_choice}, computer final cards: {computer_choice}, computer score : {sum_computer_choice}
                "You lose 😤""")
            elif sum_computer_choice >= 21:
                print(f"""Your final cards: {your_choice}, your final_score : {sum_your_choice}, computer final cards: {computer_choice}, computer score : {sum_computer_choice}
                "Opponent went over. You win 😁""")
            elif sum_computer_choice == sum_your_choice:
                print(f"""Your final cards: {your_choice}, your final_score : {sum_your_choice}, computer final cards: {computer_choice}, computer score : {sum_computer_choice}
                It's a draw""")
        elif game_start == 'n':
            print("You have decided not to play the game")
            break
        else:
            print("Enter proper input value")

game_start()