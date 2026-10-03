def calculate_average(numbers: list) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return sum(numbers) / len(numbers)


# Test case 1
print(calculate_average([10, 20, 30, 40]))

# Test case 2
print(calculate_average([5, 10, 15]))

# Test case 3 - Empty list
try:
    print(calculate_average([]))
except ValueError as e:
    print("Error:", e)