def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if input dct is a python's dictionary in key-value pair format {"key": "value"}, if not return -1
    if not isinstance(dct, dict):
        return -1

    # If key exists, print original value
    if key in dct:
        print("Original value:", dct[key])
    
    # Update dictionary
    dct[key] = value
    
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:

# - {}, "name", "Alice"
# Since dct {} is empty, it would not print the Original value, and would add the new key-value pair "name" and "Alice" to the dictionary and return it. 
result1 = update_dictionary({}, "name", "Alice")
print("Result 1:", result1)   

# - {"age": 25}, "age", 26
# The dct {"age": 25} contains the key "age" and the original value 25, it would print the original value.Then having the same key "age" with the new value 26 will update the existing key-value pair and return the updated dictionary.
result2 = update_dictionary({"age": 25}, "age", 26)
print("Result 2:", result2) 