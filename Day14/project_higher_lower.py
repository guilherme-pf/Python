from unicodedata import name
from art import logo
from art import vs
from game_data import data
import random
import sys, os

os.system("cls")

rand_A = random.randrange(0,50)

rand_B = random.randrange(0,50)

while rand_A == rand_B:
    B = random.randrange(0,50)

player_score = 0


A = rand_A
B = rand_B


name_A = data[A]["name"]
follower_count_A = data[A]["follower_count"]
description_A = data[A]["description"]
country_A = data[A]["country"]

name_B = data[B]["name"]
follower_count_B = data[B]["follower_count"]
description_B = data[B]["description"]
country_B = data[B]["country"]

game_ended = False

print(logo)
print(f"Compare A: {name_A}, a {description_A}, from {country_A}.")
print(vs)
print(f"Compare B: {name_B}, a {description_B}, from {country_B}.")
player_answer = input("Who has more followers? 'A' or 'B': ").lower()

print(logo)

while game_ended == False:

    if follower_count_A > follower_count_B:
        correct_answer = "a"
        A = A
        B = random.randrange(0,50)
        while A == B:
            B = random.randrange(0,50)

        name_A = data[A]["name"]
        follower_count_A = data[A]["follower_count"]
        description_A = data[A]["description"]
        country_A = data[A]["country"]

        name_B = data[B]["name"]
        follower_count_B = data[B]["follower_count"]
        description_B = data[B]["description"]
        country_B = data[B]["country"]
    else:
        correct_answer = "b"
        A = B
        while A == B:
            B = random.randrange(0,50)

        name_A = data[A]["name"]
        follower_count_A = data[A]["follower_count"]
        description_A = data[A]["description"]
        country_A = data[A]["country"]

        name_B = data[B]["name"]
        follower_count_B = data[B]["follower_count"]
        description_B = data[B]["description"]
        country_B = data[B]["country"]

    if player_answer == correct_answer:
        player_score += 1
    
        os.system("cls")
        print(logo)
        print(f"You're right! Current score {player_score}.")
        print(f"Compare A: {name_A}, a {description_A}, from {country_A}.")
        print(vs)
        print(f"Compare B: {name_B}, a {description_B}, from {country_B}.")
        player_answer = input("Who has more followers? 'A' or 'B': ").lower()

    else:
        game_ended = True
        os.system("cls")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {player_score}.")










