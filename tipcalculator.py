print("Welcome to tip calculator")
bill = float(input("What was the total bill? $ "))
tip = ((float(input("What percentage tip you would like to give? 10, 12 or 15? ")))/100) + 1
payers = float(input("How many people to split the bill? "))
total_per_person = round(float((bill * tip))/payers, 2)
total_per_person = "{:.2f}".format(total_per_person)
print(f"Each person should pay ${total_per_person}")