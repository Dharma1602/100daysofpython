target_number = int(input("Enter a number between 0 and 1000"))
sum_even = 0
# for x in range(0, target_number +1):
#     if x % 2 == 0:
#         sum_even += x
# print(sum_even)



##################################################
for sum in range(2, target_number +1, 2):
    sum_even += sum
print(sum_even)