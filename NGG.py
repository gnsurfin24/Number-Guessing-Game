#number guessing game!
import random
import time

def play_game():
    print("Hi! Welcome to the guessing game.")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    print(f"I am going to pick a number between {lower_bound} and {upper_bound}")
    time.sleep(2)
    print("Picking a number...")
    time.sleep(3)
    correctNumber = random.randint(lower_bound, upper_bound)
    guessCount = 0

    while True:
        try:
            guess = int(input("What is your guess?: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        guessCount += 1

        if guess < correctNumber:
            print("Wrong! You need to guess Higher")
        elif guess > correctNumber:
            print("Wrong! You need to guess Lower")
        else:
            print(f"Congrats! The right answer was {correctNumber}. It took you {guessCount} guesses. Good job!")
            break

        if abs(guess - correctNumber) <= 5:
            print("Hint: You're very close!")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()