print("Welcome to Rollercoster Ride!")
height = int(input("please enter your height in CM: "))
if height >= 120:
    print("You can Ride")
    age = int(input("What is your age? "))
    if age < 10:
        print(f"Your ride costs you ${7}")
    elif age > 18:
        print(f"Your ride costs you ${15}")
    elif 100 < age > 60:
        print(f"Your ride costs you ${5}")
    else:
        print(f"Your ride costs you ${10}")
    
else:
    print("Sorry, you are not eligible for this ride")