import random



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