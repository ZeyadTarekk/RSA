import random


def generate_e(phi):
    """
    Generate a value for the public exponent e based on the value of phi.
    The value of e should be coprime to phi and within the range 1 < e < phi.
    """
    # choose a random number between 2 and phi-1
    e = random.randint(1, phi)
    # check if e is coprime with phi using the are_coprime function
    while not are_coprime(e, phi):
        e = random.randint(1, phi)
    return e

def gcd(a, b):
    """
    Calculate the gcd of two numbers a and b using the Euclidean algorithm.
    """
    # make sure a is greater than or equal to b
    if b > a:
        a, b = b, a
    # calculate the gcd using the Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    # the gcd is the value of a
    return a

def are_coprime(a, b):
    """
    Check if two numbers a and b are coprime (have no common factors other than 1).
    """
    # calculate the gcd of a and b using the gcd function
    g = gcd(a, b)
    # if gcd(a, b) is 1, then a and b are coprime
    return g == 1