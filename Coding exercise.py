# BMI
weight = 85
height = 1.85
Bmi = weight / (height ** 2)

print("Welcome to the Bmi calculator!")
height = float(input("What is you height?"))
weight = int(input("What is your weight?"))


if Bmi < 18.5:
    print("Underweight")
elif 18.5 <= Bmi < 25:
    print("Normal weight")
else:
    print("Overweight")




