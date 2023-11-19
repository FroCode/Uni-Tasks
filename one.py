def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        perimeter = a + b + c
        s = perimeter / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return True, perimeter, area
    else:
        return False, 0, 0
a = float(input("Enter the length a: "))
b = float(input("Enter the length b: "))
c = float(input("Enter the length side c: "))

result, perimeter, area = is_triangle(a, b, c)

if result:
    print(f"Perimeter {perimeter:.2f} and area {area:.2f}.")
else:
    print("These sides cannot form a triangle.")
