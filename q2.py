def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check whether lst is a list
    if not isinstance(lst, list):
        return 
      
    # If lst is a list, iterate through it and replace occurrences of (find_val) with (replace_val). len(lst) is used to get the number of elements in the list, and range() produces a sequence of integers from 0 up to len(lst) to access each element of the list using its index.
    for i in range(len(lst)):       
        if lst[i] == find_val:
            lst[i] = replace_val
    
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

# - [1, 2, 3, 4, 2, 2], 2, 5
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Result 1:", result1) # Since this list (1st) is a list, the find_and_replace function will find all the value 2 (find_val) in the list and replace them with 5 (replace_val). 

# - ["apple", "banana", "apple"], "apple", "orange"
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Result 2:", result2) # Since this list (1st) is a list, the find_and_replace function will find all the value "apple" (find_val) in the list and replace them with "orange" (replace_val).
