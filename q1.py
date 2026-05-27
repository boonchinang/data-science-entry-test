def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Using isinstance function to check whether x and y are numeric (int or float), if not numeric return -1
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
   # If both x and y are numeric, swap them using python's tuple unpacking.
    x, y = y, x
    print("Swapped values:", x, y)
    return x, y

# Task 2
# Invoke the function "swap" using the following scenarios:

# - "Apple", 10
# Since Apple is a string and not an int nor a float, the function would return -1 and not swap the values
result1 = swap("Apple", 10)
print("Result:", result1)

# - 9, 17
# Since 9 and 17 are integers, the function would swap them
result2 = swap(9, 17)
print("Result:", result2)
