#                                                           Task 1: Simple Calculator
def simple_calculator(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
user_input = input("<input:> ")
output = simple_calculator(user_input)
print(f"<output:> {output}")

#                                                               Task 2: Fibonacci Sequence

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
n = int(input("Enter value of n: "))
result = fibonacci_sequence(n)
print(result)

#                                                           Task 3: Count Duplicates
def count_duplicates(arr):
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    duplicate_count = sum(count > 1 for count in count_dict.values())
    return duplicate_count

# Example usage:
arr = [1, 2, 3, 2, 4, 5, 1, 6, 7, 8, 6]
result = count_duplicates(arr)
print(result)

#                                                        Task 4: Copy Non-Duplicates
def copy_non_duplicates(arr):
    unique_values = []
    seen_values = set()

    for num in arr:
        if num not in seen_values:
            unique_values.append(num)
            seen_values.add(num)

    return unique_values

# Example usage:
arr = [1, 2, 3, 2, 4, 5, 1, 6, 7, 8, 6]
result = copy_non_duplicates(arr)
print(result)



#                                                        Task 5: Reverse Array In Place

def reverse_array_in_place(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage:
arr = [2, 5, 8, 4, 5]
reverse_array_in_place(arr)
print(arr)
