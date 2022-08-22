import random

while True:
    try:
        print("Welcome to the Password Generator!")
        number_letters = int(input("How many letters would you like in your password?\n"))
        number_symbols = int(input("How many symbols would you like in your password?\n"))
        number_numbers = int(input("How many numbers would you like in your password?\n"))

        if (number_letters >= 0) and (number_symbols >= 0) and (number_numbers >= 0):
            break
    except:
        print("", end="")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []



for i in range(int(number_numbers)):
    password.append(numbers[random.randint(0, len(numbers) - 1)])

for i in range(int(number_symbols)):
    password.append(symbols[random.randint(0, len(symbols) - 1)])

for i in range(int(number_letters)):
    password.append(letters[random.randint(0, len(letters) - 1)])

random.shuffle(password)

for i in range(len(password)):
    print(password[i], end="")