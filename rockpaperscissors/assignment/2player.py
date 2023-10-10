# define the function
def janken():
    # welcome message
    print("Welcome to the Rock Paper Scissors game!")

    # set players' names
    p1_name = input("Player 1, please enter your name: ")
    p2_name = input("Player 2, please enter your name: ")

    # set variables to null
    p1_score = 0
    p2_score = 0
    p1_choice = None
    p2_choice = None
    
    # cool ASCII
    ascii = """
        _______
    ---'   ____)
          (_____)
          (_____)            Guu
           (____)
    ---.___(___)
            
        ________
    ---'    ____)_____
                ______)
                _______)       Paa
                _______)
    ---.___________)

        _______
    ---'   ____)____
            ________)_
            __________)       Choki
          (____)
    ---.__(___)"""
    
    while True:
        # accept input choices from both players
        p1_choice = input(f"{p1_name}, please choose rock (r), paper (p), or scissors (s): ").lower()
        # error handling p1 for string besides r/p/s
        while p1_choice not in ["r", "p", "s"]:
            p1_choice = input(f"Invalid choice. {p1_name}, please choose r, p, or s: ").lower()
        p2_choice = input(f"{p2_name}, please choose rock (r), paper (p), or scissors (s): ").lower()
        # error handling p2 for string besides r/p/s
        while p2_choice not in ["r", "p", "s"]:
            p2_choice = input(f"Invalid choice. {p2_name}, please choose r, p, or s: ").lower()

        # account for all possibilities
        if p1_choice == p2_choice:
            # handle a tie event
            print(ascii) 
            print("") 
            print("<<<<< We have ourselves a Tie! >>>>>")
        elif (p1_choice == "r" and p2_choice == "s") or (p1_choice == "p" and p2_choice == "r") or (p1_choice == "s" and p2_choice == "p"):
            # if player 1 wins, print message and add +1 to score                 
            print(ascii) 
            print("") 
            print(f">>>>>> {p1_choice} beats {p2_choice}... {p1_name} wins this round!")
            print("")              
            p1_score += 1
        else:
            # if player 2 wins, print message and add +1 to score
            print(ascii) 
            print("")             
            print(f">>>>>> {p2_choice} beats {p1_choice}... {p2_name} wins this round!")
            print("")              
            p2_score += 1

        # display score
        print(f"{p1_name}'s score: {p1_score}")
        print(f"{p2_name}'s score: {p2_score}")

        play_again = input("Play again? (y/n)")
        while play_again not in ["y", "n"]:
            play_again = input(f"(y)es or (n)o ?").lower()       
        if play_again.lower() == 'n':
            break

    # display an exit message
    print("Thanks for playing Janken!")

# play again, repeat the function until break triggered
janken()
