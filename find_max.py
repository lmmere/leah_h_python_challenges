def find_max(numbers):
    if not numbers:
        return None  # Optional: handle empty list

    max_value = numbers[0]  # Start with the first number
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Output: 9
print(find_max([-10, -20, -3, -4]))  # Output: -3
