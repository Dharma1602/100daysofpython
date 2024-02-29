height = float(input("Please enter your height meters\n"))
weight = int(input("Please enter your weight\n"))

BMI = int(weight / height ** 2)
if BMI > 30:
    print(f"Your BMI is: {BMI}, you are slightly overweight")
    if BMI < 25:
        print(f"Your BMI is {BMI}, You are Underweight")
    elif BMI > 50:
        print(f"Your BMI is {BMI}, See a Doctor")
    elif BMI > 40:
        print(f"Your BMI is {BMI}, you are obeese")
else:
    print(f"Your BMI is {BMI}, You are Healthy")
