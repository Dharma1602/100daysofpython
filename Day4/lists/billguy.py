# names = names.string.split(", ")
# names = names_string.split(", ")
name = input("Please enter the names with a , sepearing the names: \n")
names = name.split(" ")
import random
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "is going to pay buy the meal today")
