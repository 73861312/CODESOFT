import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    # User Input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        play_game()
        return

    # Computer Selection
    computer_choice = random.choice(choices)

    # Game Logic
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    # Display Result
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()