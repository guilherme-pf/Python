from itertools import count


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2

true_count = names.lower().count('t') + names.lower().count('r') + names.lower().count('u') + names.lower().count('e')
love_count = names.lower().count('l') + names.lower().count('o') + names.lower().count('v') + names.lower().count('e')

final_number = int(str(true_count) + str(love_count))

if final_number < 10 or final_number > 90:
    print(f"Your score is {final_number}, you go together like coke and mentos.")

elif final_number > 40 and final_number < 50:
    print(f"Your score is {final_number}, you are alright together.")

else:
    print(f"Your score is {final_number}.")
