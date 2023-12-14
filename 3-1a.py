import random
import math

def isPrime(n):
    # To check if all user inputs are prime numbers
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def keyGen(p,q):

    if not (isPrime(p) and isPrime(q)):
        raise ValueError("Both p and q must be prime numbers.")

    n = p * q #Calculate n

    totient = (p-1) * (q-1) #Calculate totient of n

    e = random.randrange(2, totient) #Generating a random number public key e

    while math.gcd(e, totient) != 1:
        e = random.randrange(2, totient)  #To make sure e is coprime to totient

    d = pow(e, -1, totient) # Find multiplicative inverse of of e modulo

    return (e,d)

try:
    p = int(input("Enter a large prime number (p): "))
    q = int(input("Enter another large prime number (q): "))

    RSA_key_pair = keyGen(p, q)
    print("RSA Key Pair:", RSA_key_pair)
except ValueError as e:
    print(f"Error: {e}")


    





