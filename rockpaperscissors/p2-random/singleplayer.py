import random

def play_game():
    # welcome message
    print("Welcome to the Rock Paper Scissors game!")

    # read players' names
    p1_name = input("p1, please enter your name: ")
    p2_name = input("p2, please enter your name: ")

    # initialize score
    p1_score = 0
    p2_score = 0
    p1_choice = None
    p2_choice = None
    while True:
        # accept input choices from both players
        p1_choice = input(f"{p1_name}, please choose rock, paper, or scissors: ").lower()
        p2_choice = random.choice(["rock", "paper", "scissors"])

        # account for all possibilities
        if p1_choice == p2_choice:
            # tie
            print("Tie!")
        elif (p1_choice == "rock" and p2_choice == "scissors") or (p1_choice == "paper" and p2_choice == "rock") or (p1_choice == "scissors" and p2_choice == "paper"):
            # player 1 wins
            print(f"{p1_name} wins!")
            p1_score += 1
        else:
            # player 2 wins
            print(f"{p2_name} wins!")
            p2_score += 1

        # display output score
        print(f"{p1_name} score: {p1_score}")
        print(f"{p2_name} score: {p2_score}")

        play_again = input("Do you want to play again? (y/n)")
        if play_again.lower() == 'n':
            break

    # display a "Thank you for playing" message
    print("Thank you for playing!")

play_game()
