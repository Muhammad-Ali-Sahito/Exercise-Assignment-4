import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts_left = 5

    while attempts_left > 0:
        # Get user's guess
        user_guess = int(input("Enter your guess between 1 and 100: "))
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print("Congratulations! You guessed the number.")
            return
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        
        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    print(f"Game over! You ran out of guesses. The correct number was {secret_number}.")

# Call the function to start the game
guess_the_number()
