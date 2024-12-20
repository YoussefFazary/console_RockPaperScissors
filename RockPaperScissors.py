import random

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

rock_paper_scissors = ["rock", "paper", "scissors"]

player_choice = input("Choose Rock, Paper, or Scissors\n").lower()
if not (player_choice == "rock" or player_choice == "scissors" or player_choice == "paper"):
    print("You've entered the wrong value,\n")
    input("press the enter button to exit")
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

    input("press the enter button to exit")