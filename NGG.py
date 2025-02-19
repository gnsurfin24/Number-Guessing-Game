#number guessing game!
import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100")
time.sleep(2)
print("Picking a number...")
time.sleep(3)
guess = int(input("What is your guess?: "))
correctNumber = random.randint(1, 100)
guessCount = 1

while guess != correctNumber:
    guessCount += 1
    if guess < correctNumber:
        print("Wrong! You need to guess Higher")
    else:
        print("Wrong! You need to guess Lower")
    guess = int(input("What is your guess?: "))



print(f"Congrats! The right answer was {correctNumber}. It took you {guessCount} guesses. Good job!")