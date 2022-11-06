import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

game_list = [rock, paper, scissors]

while True:
    try:
        players_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
        if players_input >=00 and players_input < 3:
            break
    except:
        print("", end="")

players_choice_str = choices[players_input]
computers_choice_int = random.randint(0,2)
computers_choice_str = choices[computers_choice_int]

print("You chose:", game_list[players_input])
print("Computer chose:", game_list[computers_choice_int])

if (players_input == computers_choice_int):
    print("It is a tie.")
elif (players_input == 0 and computers_choice_int == 1) or (players_input == 1 and computers_choice_int == 2) or (players_input == 2 and computers_choice_int == 0):
    print("You lose")
else:
    print("You win!")




