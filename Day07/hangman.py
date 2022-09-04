from random import randint, random
from hangman_art import stages, logo
from hangman_words import word_list
import sys, os

print(logo)
i = randint(0,len(word_list)-1)

word = word_list[i]

char_list = list(word)

solution = []

for i in word:
    solution.append("_")

player_guesses = []

player_lives = 0

while ("_" in solution) and (player_lives < 6):

    guess = input("Guess letter: ").lower()
    os.system("cls")

    if guess not in player_guesses:

        if guess not in word:
            player_lives += 1
            print(f"{' '.join(solution)}")
            print(f"The letter '{guess}' is not in the word")
            print((stages[6-player_lives]))
            player_guesses += guess

        else:
            for i in range(len(char_list)):
                if guess == char_list[i]:
                    solution[i] = guess

            print(f"{' '.join(solution)}")
            print((stages[6-player_lives]))
            player_guesses += guess

    else:
        print(f"{' '.join(solution)}")
        print(f"You've already guessed the letter {guess}!")
        print((stages[6-player_lives]))


if player_lives == 6:
    print("You Lost")
    print(f"The word was {word}")
else:
    print("You won!")