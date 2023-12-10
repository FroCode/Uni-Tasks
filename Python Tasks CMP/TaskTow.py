# A. Read 10 integers from the user and write them into the Tab1 array
Tab1 = []
for _ in range(10):
    user_input = int(input("Enter an integer (enter 0 to terminate input): "))
    if user_input == 0:
        break
    Tab1.append(user_input)

# B. Determine the sum and average of the numbers and print them along with Tab1 array elements
sum_tab1 = sum(Tab1)
average_tab1 = sum_tab1 / len(Tab1) if len(Tab1) > 0 else 0

print("\nTab1 array elements:", Tab1)
print("Sum of numbers:", sum_tab1)
print("Average of numbers:", average_tab1)

# C. Add an option to terminate input if the user enters 0
if len(Tab1) < 10:
    print("\nInput terminated early as the user entered 0.")
