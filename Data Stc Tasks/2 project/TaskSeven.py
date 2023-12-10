def find_minimum(arr, start, end):
    if start == end:
        return arr[start]  # Base case: array has only one element

    mid = (start + end) // 2

    # Recursive calls to find the minimum in each half
    min_left = find_minimum(arr, start, mid)
    min_right = find_minimum(arr, mid + 1, end)

    # Combine results to find the overall minimum
    return min(min_left, min_right)

# Example usage:
array = [5, 3, 9, 1, 7, 2, 8, 4, 6]
result = find_minimum(array, 0, len(array) - 1)
print(result)
