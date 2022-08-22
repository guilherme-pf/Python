student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = student_scores[0]
for i in range(len(student_scores)):
    if student_scores[i] > max_score:
        max_score = student_scores[i]
print(f"The highest score in the class is: {max_score}")