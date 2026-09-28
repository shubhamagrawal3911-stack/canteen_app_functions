# A school stores students grades in a nested list whre each inner list represents a student's score




students_grades = 1
[85, 90, 78, 92]
[60, 65, 70, 72]
[95, 98, 100, 96]
[80, 82, 88, 84]
    
    
# Task 1 & 2: Calculate indivisual averages and find top student
highest_avg = 0
top_student_index = -1
all_scores = []

for idx, grades in enumerate(student_grades):
    student_avg = sum(grades) / len(grades)
    all_scores.extend(grades)
    print(f"student (idx) Average: (student_avg:.2f)")
    
    if student_avg > highest_avg:
        highest_avg = student_avg
        top_student_index = idx
        
print(f"\nTop Performing Student: Student (top_student_index) with an average of (highest_avg:.2f):")


# Task 3: Class average overall
class_avg = sum(all_scores) / len(all_scores)
print(f"Overall Class Average: (class_avg:.2f)")


# Task 1: Imitialize double -precision flaoting-posting array
team