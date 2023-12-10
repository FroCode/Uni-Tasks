def power_iterative(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

# Example: Calculate the power of 2^3
result_iterative = power_iterative(2, 3)
print(result_iterative)

def power_recursive(a, n):
    if n == 0:
        return 1
    else:
        return a * power_recursive(a, n - 1)

# Example: Calculate the power of 2^3
result_recursive = power_recursive(2, 3)
print(result_recursive)

def Power1(a, n):
    if n == 1:
        return a
    else:
        m = n // 2
        return Power1(a, m) * Power1(a, n - m)

# Example: Calculate the power of 2^3 using Power1
result_Power1 = Power1(2, 3)
print(result_Power1)
