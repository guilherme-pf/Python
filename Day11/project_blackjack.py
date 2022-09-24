from os import remove
from art import logo
import random


play = input("Do you want to play a game of Blackhack? Type 'y' or 'n': ").lower()

if play == "y":
    print(logo)



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = []
computers_cards = []

def blackjack():
    player_card1 = random.choice(cards)
    player_card2 = random.choice(cards)
    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)

    players_cards.extend([player_card1, player_card2])
    computers_cards.extend([computer_card1,computer_card2])

    player_score = sum(players_cards)
    computer_score = sum(computers_cards)

    if player_score > 21 and 11 in players_cards:
        players_cards.remove(11)
        players_cards.append(1)

    if computer_score > 21 and 11 in computers_cards:
        computers_cards.remove(11)
        computers_cards.append(1)

    player_score = sum(players_cards)
    computer_score = sum(computers_cards)

    print(f"Your cards: {players_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_card1}")

    draw = "y"

    while player_score <= 21 and draw == "y":
        draw = input("Type 'y' to get another card, type 'n' to pass: ")

        if draw == "y":
            player_card = random.choice(cards)
            players_cards.append(player_card)
            
            player_score = sum(players_cards)

            if player_score > 21 and 11 in players_cards:
                players_cards.remove(11)
                players_cards.append(1)

            player_score = sum(players_cards)

            print(f"Your cards: {players_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_card1}")


    while computer_score < 17:
        computer_card = random.choice(cards)
        computer_score += computer_card
        computers_cards.append(computer_card)

        if computer_score > 21 and 11 in computers_cards:
            computers_cards.remove(11)
            computers_cards.append(1)

            computer_score = sum(computers_cards)

    computer_score = sum(computers_cards)

    if player_score == computer_score:
        print(f"Your cards: {players_cards}, current score: {player_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
        print("Draw 🙃")

    elif player_score > 21:
        print(f"Your cards: {players_cards}, current score: {player_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
        print("You went over you lose 😒")
    
    elif computer_score > player_score and computer_score <= 21:
        print(f"Your cards: {players_cards}, current score: {player_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
        print("You lose 😒")
    else:
        print(f"Your cards: {players_cards}, current score: {player_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
        print("You win 😀")
            
blackjack()

