#Playfair cipher
def breakDown(c, p):
    # Create a matrix containing lists
    grid = [["a", "b", "c", "d", "e"],
            ["f", "g", "h", ["i", "j"], "k"],
            ["l", "m", "n", "o", "p"],
            ["q", "r", "s", "t", "u"],
            ["v", "w", "x", "y", "z"]]

    # Replace 'j' with 'i' and vice versa
    c = 'i' if c == 'j' else ('j' if c == 'i' else c)

    coordinates = None # Initialize coordinates to None
    for i in range(5):
        for j in range(5):
            if c in grid[i][j]:
                coordinates = (i, j) # Update coordinates when the character is found
                break
      # After the loop, coordinates will either contain the grid coordinates or remain None if the character was not found.
                
    # Return the result as a string
    return p[coordinates[0]] + p[coordinates[1]]

# Use case:
p = "qwert"
#print(breakDown('g', p))  # Output: "ww"
#print(breakDown('v', p))  # Output: "tq"

user_input = input("Enter a character: ").lower()
result = breakDown(user_input, p)
print(f"Result: {result}")