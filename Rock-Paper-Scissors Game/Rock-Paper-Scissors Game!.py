import random  # Importing the random module for computer choice selection

def get_winner(player, computer):
    """Function to determine the winner based on the game rules."""
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    # else:
        return "computer"

choices = ["rock", "paper", "scissors"]  # List of possible choices
rounds = 10  # Maximum number of rounds
player_wins = 0  # Counter for user wins

print("\nWelcome to the Rock-Paper-Scissors Game! 🎮")  # Game introduction

for round_num in range(1, rounds + 1):  # Looping through 10 rounds
    print(f"\nRound {round_num} of {rounds}")  # Display current round
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()  # User input

    if player_choice not in choices:  # Check if input is valid
        print("Invalid choice, try again.")  
        continue  # Skip to the next iteration if input is incorrect

    computer_choice = random.choice(choices)  # Computer selects randomly
    print(f"Computer chose: {computer_choice}")  # Display computer's choice

    result = get_winner(player_choice, computer_choice)  # Get game result

    if result == "player":  # Check if player wins
        print("You win this round! 🎉")
        player_wins += 1  # Increment player win count
    elif result == "computer":
        print("Computer wins this round! 🤖")
    else:
        print("It's a tie! ⚖️")

# Display final results after all rounds
print("\nGame Over! Thanks for playing. 😊")
print(f"You won {player_wins} out of {rounds} rounds!")  # Show total user wins