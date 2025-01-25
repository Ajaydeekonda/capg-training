import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    
    target_number = random.randint(1, 100)
    
    attempts = 0
    
    while True:
        
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        
        if guess < target_number:
            print("Too Low! Try again.")
        elif guess > target_number:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {target_number} in {attempts} attempts.")
            break  

if __name__ == "__main__":
    number_guessing_game()
