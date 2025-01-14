This is a Python implementation of the classic game Rock, Paper, Scissors. The program allows a user to play against the computer. It features the following functionality:

Getting User Input:
The get_user_choice function prompts the user to select an option: Rock, Paper, or Scissors. It ensures valid input by repeating the prompt until the user enters a valid choice (1, 2, or 3).

Computer's Random Choice:
The get_computer_choice function randomly selects an option for the computer using Python's random.randint.

Determining the Winner:
The determine_winner function compares the user's choice and the computer's choice to determine the winner based on the rules of the game:

Rock beats Scissors.
Scissors beat Paper.
Paper beats Rock.
If both choices are the same, it's a tie.
Game Loop:
The play_game function provides a user-friendly interface to play the game. The user can play multiple rounds by choosing to play again after each round. The loop continues until the user decides to quit.

Exit Message:
At the end of the game, the program thanks the user for playing.
