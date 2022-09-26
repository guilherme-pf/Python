from art import logo
import random

print(logo)
number = random.randrange(1,100)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")


while True:
    try:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy" or difficulty == "hard":
            break
    except:
        print("", end="")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")   

player_guess = 0

while (player_guess != number) and (attempts > 0):
    player_guess = int(input("Make a guess: "))
    if player_guess > number:
        attempts -= 1
        print("Too high\nGuess again.")
        print(f"You have {attempts} attempts remaining to guess the number.") 
    elif player_guess < number:
        attempts -= 1
        print("Too low\nGuess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")


if player_guess == number:
    print(f"You got it! The answer was {number}.")
else:
    print(f"You've run out of guesses, you lose. The number was {number}")