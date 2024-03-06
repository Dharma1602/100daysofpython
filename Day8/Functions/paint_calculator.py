import math
def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You will need {round_up_cans} cans of paint")

h = int(input("Enter the height of the wall: \n"))
w = int(input("Enter the width of the wall: \n"))
coverage = 5

paint_calc(height=h, width=w, cover=coverage)

