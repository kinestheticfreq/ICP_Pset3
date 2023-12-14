def nextLevel(s, k):
    result = ""
    for i in range(len(s)):
        element = s[i]
        key = k % 26  # Ensure the key is within the range of the alphabet
        shifted_element = chr(((ord(element) - ord('a') + key) % 26) + ord('a'))
        result += shifted_element
        k = ord(element) - ord('a')  # Set the key for the next iteration

    return result

# Take user input for string s and key k
s = input("Enter the string: ")
k = int(input("Enter the key: "))

# Call the function with user input
result = nextLevel(s, k)

# Display the result
print("Solution:", result)
