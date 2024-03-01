
total_height = 0
number_of_students = 0


student_heights = input("Enter all the height is students in CM").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


for height in student_heights:
    total_height += height
print(f"total height = {total_height}")


for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"Average height of students in the classsroom is {average_height}")