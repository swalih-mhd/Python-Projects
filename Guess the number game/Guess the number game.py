import random  # Importing the random module to generate a random number

def play_game():
    number = random.randint(1, 10)  # Generate a random number between 1 and 10
    attempts = 0  # Counter to track the number of attempts
    max_attempts = 7  # Maximum number of attempts allowed

    print("\n Welcome to Guess the Number!") 
    print("I have chosen a number between 1 and 10. Try to guess it!") 

    while attempts < max_attempts:  # Loop until max attempts are reached
        try:
            # Taking user input and converting it to an integer
            guess = int(input(f"Attempt {attempts+1}/{max_attempts}: Enter your guess: "))  
        except ValueError:  # If input is not a number, handle the error
            print("Invalid input! Please enter a number.")  
            continue

        attempts += 1  # Increase the attempt count

        if guess < number:  # Check if the guess is too low
            print("Too low!")
        elif guess > number:  # Check if the guess is too high
            print("Too high!")
        else:  # If the guess is correct
            print(f"Correct! You guessed it in {attempts} tries.")  
            break 

    else:  # If max attempts are reached and the user didn't guess correctly
        print(f"Game over! The number was {number}.")  

    # Ask if the user wants to play again
    if input("\nDo you want to play again? (yes/no): ").lower() == 'yes':  
        play_game()  # Restart the game if the user says "yes"
    else:
        print("Thanks for playing!")

play_game()   # Start the game

