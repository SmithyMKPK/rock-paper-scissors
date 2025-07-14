# Rock Paper Scissors Game
# Copilot Prompt: Create a simple Rock Paper Scissors game using Pygame. Make it interactive with buttons for each choice and display the result of each round.

# Rock Paper Scissors Game
# Copilot Prompt:
# Create a simple Rock Paper Scissors game in Python.
# The game should:
# - Ask the user to type their choice (Rock, Paper, or Scissors) in the terminal.
# - The computer randomly selects its move.
# - Display both choices and the result (win, lose, or tie).
# - Repeat until the user types 'quit'.
#
# As a web version, see #file:1_web_recap.html for an HTML/JS implementation.


import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("Type Rock, Paper, Scissors or 'quit' to exit: ").strip().capitalize()
    if user_input == "Quit":
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose: {user_input}")
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!\n")
    elif (
        (user_input == "Rock" and computer_choice == "Scissors") or
        (user_input == "Paper" and computer_choice == "Rock") or
        (user_input == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!\n")
    else:
        print("You lose!\n")