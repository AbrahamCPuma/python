# Let's use the data structure from the exercise: a list of dictionaries.
# This is a more common and flexible way to handle records.
# Each dictionary represents a single student.
# I've also converted the scores from strings to floats here.
students = [
    {'name': 'Abraham', 'scores': [40.0, 30.4, 100.3]},
    {'name': 'Jesus', 'scores': [90.0, 70.5, 50.5]},
    {'name': 'Beto', 'scores': [100.0, 110.0, 70.8]} # Note: I capitalized Beto for consistency
]

print(f'-----------Starting Data-----------\n{students}\n')

# It's good practice to have functions accept data as parameters
# instead of using global variables.
def calculate_and_assign_grades(student_list):
    """
    Calculates average scores and assigns grades for a list of students.
    This function modifies the dictionaries in the list directly.
    """
    # Loop through each student dictionary in the list.
    for student in student_list:
        # The scores are already floats, so no conversion is needed here.
        scores = student['scores']
        average = sum(scores) / len(scores)

        # Add the 'average' to the student's dictionary
        student['average'] = round(average, 2)

        # Determine the letter grade based on the average
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        # Add the 'grade' to the student's dictionary
        student['grade'] = grade
    return student_list

# Call the function with the student data and store the result.
graded_students = calculate_and_assign_grades(students)

print('-----------Final Results-----------')
# Loop through the updated list of students and print their final grades.
for student in graded_students:
    print(f"Name: {student['name']}, Average: {student['average']}, Grade: {student['grade']}")
