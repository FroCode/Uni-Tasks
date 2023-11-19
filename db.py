# Program to Determine Arithmetic Mean of Student Grades

def calculate_grade_information(grades):
    num_grades = len(grades)
    average = sum(grades) / num_grades

    if average <= 3.25:
        grade_info = "Satisfactory"
    elif 3.26 <= average <= 3.75:
        grade_info = "Satisfactory+"
    elif 3.76 <= average <= 4.25:
        grade_info = "Good"
    elif 4.26 <= average <= 4.60:
        grade_info = "Good+"
    elif 4.61 <= average <= 4.80:
        grade_info = "Very Good"
    else:
        grade_info = "Excellent"

    return num_grades, average, grade_info

# Input grades using command line
grades = []
while True:
    try:
        grade = float(input("Enter a grade (or type 'done' to finish): "))
        if grade < 2.0 or grade > 5.0:
            print("Invalid grade. Please enter a grade between 2.0 and 5.0.")
            continue
        if grade == 'done':
            break
        grades.append(grade)
    except ValueError:
        print("Invalid input. Please enter a valid numeric grade.")

num_grades, average, grade_info = calculate_grade_information(grades)

print(f"\nNumber of grades: {num_grades}")
print(f"Average grade: {average:.2f}")
print(f"Grade Information: {grade_info}")

# Horner's Scheme for Polynomial Evaluation

def horner_scheme(coefficients, x):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result = result * x + coefficients[i]
    return result

# Examples
# a)
coefficients_a = [2, 0, 0, -3, 0, 5, -1]
x_a = -2
result_a = horner_scheme(coefficients_a, x_a)
print(f"\nResult for a): {result_a}")

# b)
coefficients_b = [2, 0, 0, -3, 0, 5, -1]
x_b = 3
result_b = horner_scheme(coefficients_b, x_b)
print(f"Result for b): {result_b}")

# c)
coefficients_c = [2, -4, 3, 1]
x_c = 2
result_c = horner_scheme(coefficients_c, x_c)
print(f"Result for c): {result_c}")

# d)
coefficients_d = [-1, 0, 2, 0, 3, 5]
x_d = -2
result_d = horner_scheme(coefficients_d, x_d)
print(f"Result for d): {result_d}")
