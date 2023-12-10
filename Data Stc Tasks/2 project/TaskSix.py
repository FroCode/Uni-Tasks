def exponentiation_by_squaring(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_pow = exponentiation_by_squaring(base, exponent // 2)
        return half_pow * half_pow
    else:
        half_pow = exponentiation_by_squaring(base, (exponent - 1) // 2)
        return base * half_pow * half_pow

# Example: Calculate the power of 2^5 using exponentiation by squaring
result = exponentiation_by_squaring(2, 5)
print(result)
