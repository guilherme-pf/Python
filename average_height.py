student_heights = input("Input a list of student heighs ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(round(sum(student_heights)/len(student_heights)))