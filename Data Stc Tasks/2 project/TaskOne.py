def T2(n):
    if n == 1:
        return 1
    else:
        return T2(n // 2) + n

# Example: Compute T2(8)
result_T2 = T2(8)
print(f"T2(8) = {result_T2}")
