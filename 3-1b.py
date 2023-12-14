def modInvert(x, n):
    # To calculate modular multiplicative inverse of x modulo n
    gcd, inverse, _ = extendedGCD(x, n)

    if gcd == 1:
        return inverse % n
    else:
        return 0

def extendedGCD(a, b):
    # Extended Euclidean algorithm to find GCD and coefficients
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extendedGCD(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

# User input for x and n with validation
try:
    x = int(input("Enter an integer (x): "))
    n = int(input("Enter the modulus (n): "))

    result = modInvert(x, n)
    print(f"The modular inverse of {x} modulo {n} is {result}")
except ValueError as e:
    print(f"Error: {e}")
