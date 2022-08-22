height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = round(weight/height**2)

if BMI <= 18.5:
    weigh_value = "you are underweight."

elif (BMI > 18.5 and BMI <= 25):
    weigh_value = "you have a normal weight."

elif BMI >= 25 and BMI <= 30:
    weigh_value = "you are slightly overweight."

elif BMI >= 30 and BMI <= 35:
    weigh_value = "you are obese."

else:
    weigh_value = "you are clinically obese."

print(f"Your BMI is {BMI}, {weigh_value}")