
#incomplete version, missing logic to substitute 11 for 1, when sum over 21.
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

    player_score = player_card1 + player_card2
    computer_score = computer_card1 + computer_card2

    print(f"Your cards: {players_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_card1}")

    draw = "y"

    while player_score <= 21 and draw == "y":
        draw = input("Type 'y' to get another card, type 'n' to pass: ")

        if draw == "y":
            player_card = random.choice(cards)
            computer_card = random.choice(cards)
            players_cards.append(player_card)
            computers_cards.append(computer_card)
            
            player_score += player_card
            computer_score += computer_card

            print(f"Your cards: {players_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_card1}")

        else:
            while computer_score < 17 and computer_score < player_score:
                computer_card3 = random.choice(cards)
                computer_score += computer_card3
                computers_cards.append(computer_card3)

            if player_score == computer_score:
                print(f"Your cards: {players_cards}, current score: {player_score}")
                print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                print("Draw 🙃")
          
            elif computer_score > player_score and computer_score <= 21:
                print(f"Your cards: {players_cards}, current score: {player_score}")
                print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                print("You lose 😒")
            else:
                print(f"Your cards: {players_cards}, current score: {player_score}")
                print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                print("You win 😀")
                
    if player_score > 21:
        print(f"Your cards: {players_cards}, current score: {player_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
        print("You went over you lose 😒")

blackjack()
