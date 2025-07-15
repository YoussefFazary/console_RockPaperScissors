
import random


game_over = True
# ASCII art representations for "rock", "paper", and "scissors" are defined.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# A list of choices ["rock", "paper", "scissors"] is used for random selection.
rock_paper_scissors = ["rock", "paper", "scissors"]

while game_over:
    # The user is prompted to input their choice (case-insensitive: "rock", "paper", or "scissors").
    player_choice = input("Choose Rock, Paper, or Scissors\n").lower()

    # If the input is invalid, the game informs the user and exits.
    if not (player_choice == "rock" or player_choice == "scissors" or player_choice == "paper"):
        print("You've entered the wrong value,\n")
        input("press the enter button to exit")

    # The computer randomly selects one of the options using the random.choice function.
    # Both the user’s and computer’s choices are displayed alongside their corresponding ASCII art.
    # The game logic determines the winner based on standard Rock, Paper, Scissors rules:
    # --Rock beats Scissors.
    # --Scissors beat Paper.
    # --Paper beats Rock.
    else:
        computer_choice = random.choice(rock_paper_scissors)
        # print(f"the computer chose {computer_choice}")
        if computer_choice == "paper":
            print(f"Computer chose {computer_choice}\n {paper}")
        elif computer_choice == "rock":
            print(f"Computer chose {computer_choice}\n {rock}")
        elif computer_choice == "scissors":
            print(f"Computer chose {computer_choice}\n {scissors}")

        if player_choice == "paper":
            print(f"You chose {player_choice}\n {paper}")
        elif player_choice == "rock":
            print(f"You chose {player_choice}\n {rock}")
        elif player_choice == "scissors":
            print(f"You chose {player_choice}\n {scissors}")

        # A "Draw" is declared if both choices are the same.
        if player_choice == computer_choice:
            print("Draw")
        elif player_choice == "rock" and computer_choice == "paper":
            print("Computer wins")
        elif player_choice == "rock" and computer_choice == "scissors":
            print("You win")
        elif player_choice == "paper" and computer_choice == "scissors":
            print("Computer wins")
        elif player_choice == "paper" and computer_choice == "rock":
            print("You win")
        elif player_choice == "scissors" and computer_choice == "rock":
            print("Computer wins")
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win")
            
        # Check if the user wants to play again, if Y or y is chosen then the game repeats, else it exits the while loop
        play_again = input("Enter Y to play again ".lower())
        if play_again == "y":
            game_over = True
        else:
            game_over = False

# The outcome (win, lose, or draw) is announced.
# The game waits for the user to press Enter before exiting.
input("press the enter button to exit")
