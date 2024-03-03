student_scores = input("Enter the scores of all students: \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(f"Scores of all students: {student_scores}")

# highest_score = max(student_scores)

# print(f"Highest Score in the Class is {highest_score}")

highest_score = 0

for x in student_scores:
    if x > highest_score:
        highest_score = x

print(f"The highest score of the class is {highest_score}")
