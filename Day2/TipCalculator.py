print("Welcome to Tip Calculator")
bill = float(input("Please enter the Bill? $"))
tip = int(input("please enter the percentage of tip 10, 12, 15"))
people = int(input("number of people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
# finlal_bill = round(bill_per_person, 2)
final_bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_bill}")