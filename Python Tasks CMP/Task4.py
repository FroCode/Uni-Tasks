# here i used random lib 
import random

# A. Simulate throwing a dice 100 times and store the results in Tab3
Tab3 = [random.randint(1, 6) for _ in range(100)]

# B. Plot the results in console text mode as horizontal bars
print("Number of 'dice eyes' drawn for each value from 1 to 6:")
for i in range(1, 7):
    count = Tab3.count(i)
    bar = '#' * count
    print(f"{i}: {bar}")
