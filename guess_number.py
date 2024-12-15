import random

def guess(guess_limit):
    # Generate a random number between 0 and guess_limit (inclusive)
    random_number = random.randint(0, guess_limit)
    guess = None

    print(f"Welcome to the guessing game! Try to guess the number between 0 and {guess_limit}.")
    
    while guess != random_number:
        try:
            # Get user input and ensure it is an integer
            guess = input(f"Enter a number between 0 and {guess_limit}: ")
            guess = int(guess)
            
            # Provide feedback on the guess
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! The random number was {random_number}. Well done!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break

# Call the function with a guess limit
guess(5)
