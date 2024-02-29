print("Welcome to RollerCoster Ride")
height = int(input("Enter your height: \n"))
bill = 0
if height >= 120:
    print("you can ride the roller coster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Mid life crisis ticket for free, enjoy the ride")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken: Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}")
        
    
else:
    print("Sorry, you have to grow taller before you can ride")