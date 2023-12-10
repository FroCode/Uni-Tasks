def T1(n):
    if n == 1:
        return 1
    else:
        return T1(n // 2) + 1

# Example: Compute T1(8)
result_T1 = T1(8)
print(f"T1(8) = {result_T1}")


 