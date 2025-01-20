import random

def get_user_choice():
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (1/2/3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please choose again.")
        choice = input("Enter your choice (1/2/3): ")
    return int(choice)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user, computer):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose: {choices[user]}")
    print(f"Computer chose: {choices[computer]}")

    if user == computer:
        return "It's a tie!"
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    play_again = "y"
    while play_again.lower() == "y":
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (y/n): ")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
