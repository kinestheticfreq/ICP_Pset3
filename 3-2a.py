#3-2a Reverse Caesar Cipher
def revCaesar(s, k):
    outText = []

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for eachLetter in s:
        if eachLetter in alphabet:
            index = alphabet.index(eachLetter)
            decrypting = (index - k) % 26  # Perform reverse Caesar cipher decryption.
            outText.append(alphabet[decrypting])
        else:
            # Non-alphabetic characters remain unchanged.
            outText.append(eachLetter)

    return ''.join(outText)

# Get user input for s and k
s = input("Enter the string to be decrypted: ")
k = int(input("Enter the key (an integer): "))

# Call the revCaesar function with user input and print the result
decrypted_text = revCaesar(s, k)
print("Decrypted:", decrypted_text)
