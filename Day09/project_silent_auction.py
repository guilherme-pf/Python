import sys, os

bids = {}
other_bidders = "y"

while other_bidders == "y":
    os.system("cls") #clear the console
    key = input("What is your name?")
    value = int(input("What's your bid?"))
    bids[key] = value
    other_bidders = input("Are there any other bidders? y or n.\n")

highest_bid = 0
winner = ""

for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")

