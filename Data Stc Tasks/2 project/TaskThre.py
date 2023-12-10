def T3a(n):
    if n == 1:
        return 1
    else:
        return 2 * T3a(n // 2) + n

# Example: Compute T3a(8)
result_T3a = T3a(8)
print(f"T3a(8) = {result_T3a}")

def T3b(n):
    if n == 1:
        return 1
    else:
        return 2 * T3b(n // 2) + n

# Example: Compute T3b(8)
result_T3b = T3b(8)
print(f"T3b(8) = {result_T3b}")

def T3c(n):
    if n == 1:
        return 1
    else:
        return T3c(n // 2) + T3c(n // 2) + n

# Example: Compute T3c(8)
result_T3c = T3c(8)
print(f"T3c(8) = {result_T3c}")
