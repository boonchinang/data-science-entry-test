def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric 
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return

    # Check divisibility using the modulus operator, no remainder 0 means num is divisible by divisor. If there is a remainder, it means num is not divisible by divisor.
    return num % divisor == 0
    

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
result1 = check_divisibility(10, 2)
print("Result 1:", result1)   

# - 7, 3
result2 = check_divisibility(7, 3)
print("Result 2:", result2)   