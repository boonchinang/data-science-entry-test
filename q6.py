def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """

    i = 0                   # Start the index at 0
    while i < len(lst):     # Loop until the end of the list
        if lst[i] < 0:      # Check the list for any negative numbers
            return lst[i]   # If a negative number is found, return the number
        i += 1
    return "No negatives"
    


# Task 2
# Invoke the function "find_first_negative" using the following scenario:

# - [3, 5, -1, 7, -2, 8]
# The first negative number is -1, so the function would return -1.
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Result 1:", result1) 

# - [2, 10, 7, 0]
# Since there are no negative numbers in the list, the function would return "No negatives".
result2 = find_first_negative([2, 10, 7, 0])
print("Result 2:", result2)
