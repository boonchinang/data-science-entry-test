def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check whether the input s is a string
    if not isinstance(s, str):
        return
    
    # Reverse a given string using Python slicing
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# Since "Hello World" is a string, the function would return "dlroW olleH".
result1 = string_reverse("Hello World")
print("Result 1:", result1) 

# - "Python"
# "Python" is also a string, the function would return "nohtyP".  However, if the function is not a string meaning without the enclosed quotes, it would return an error.
result2 = string_reverse("Python")
print("Result 2:", result2)   