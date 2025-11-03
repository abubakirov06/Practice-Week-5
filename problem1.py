def find_best_student(student_names, student_scores):
    if student_names == [] and student_scores == []:
        return None
    else:
        maximum = 0
        name = ''
        for i in range(len(student_scores)):
            if student_scores[i] > maximum:
                maximum = student_scores[i]
                name = student_names[i]

    return name

print('\n\n')
names = ["Alice", "Bob", "Charlie", "David"]
scores = [88, 92, 99, 95]
print(f"Top student is: {find_best_student(names, scores)}")

names = ["Eve", "Frank", "Grace"]
scores = [95, 85, 95]
print(f"Top student in a tie is: {find_best_student(names, scores)}")

names = []
scores = []
print(f"Result for empty lists: {find_best_student(names, scores)}")
print('\n\n')