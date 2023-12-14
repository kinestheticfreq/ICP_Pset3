def moveAround(s, k):
    # Ensure k is within the length of the string to avoid unnecessary rotations
    k = k % len(s)
    
    # Perform the rotation
    shifted_string = s[k:] + s[:k]
    
    return shifted_string

# Take user input for the string and shift amount
user_input_s = input("Enter a string: ")
user_input_k = int(input("Enter the shift amount (k): "))

# Use case
result = moveAround(user_input_s, user_input_k)
print(result)
