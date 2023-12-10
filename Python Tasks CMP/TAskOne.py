Tab1 = []
Tab1 = list(range(1, 101))

print("Contents of the array 1..100 in 10 columns:")
for i in range(0, 100, 10):
    print('\t'.join(map(str, Tab1[i:i+10])))

print("\nContents of the array 100..1 in 10 columns:")
for i in range(99, -1, -10):
    print('\t'.join(map(str, Tab1[i:i-10 if i >= 10 else -1:-1])))
