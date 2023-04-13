import sympy
import random


def split_message(message):
    """
    Split a message into groups of 5 and pad the last group with spaces if its length is less than 5.
    """
    message = message.lower()
    # split the message into a list of characters
    chars = list(message)
    # initialize the output list
    output = []
    # loop over the characters and group them into groups of 5
    for i in range(0, len(chars), 5):
        # get the current group of 5 characters
        group = ''.join(chars[i:i+5])
        # if the group is less than 5 characters, pad it with spaces
        if len(group) < 5:
            group = group + ' '*(5-len(group))
        # add the group to the output list
        output.append(group)
    return output


splited = split_message('Hey zEyad how are you')


def convert_to_number(groups):
    """
    Convert group of message to number
    """
    # convert each group to a number
    nums = []
    for group in groups:
        num = 0
        sum_number = 0
        i = 4
        for char in group:
            if (ord(char) in range(47, 58)):
                num = ord(char) - 48
            elif (ord(char) in range(97, 123)):
                num = ord(char) - 87
            else:
                num = 36
            sum_number = sum_number + pow(37, i) * num
            i = i - 1
        nums.append(sum_number)
    return nums


def convert_to_string(number):
    """
    Convert a number to the corresponding string back
    """
    string = ''
    char = ''
    while number > 0:
        if (pow(number, 1, 37) in range(0, 10)):
            char = str(pow(number, 1, 37))
        elif (pow(number, 1, 37) in range(10, 36)):
            char = chr(pow(number, 1, 37) + 87)
        else:
            char = chr(32)
        number //= 37
        string += char
    return string[::-1]


def extended_euclidean_algo(a, b):
    """
    Returns the extended Euclidean algorithm for two given integers a and b.
    """
    if b == 0:
        return (1, 0)
    # using pow as it is much faster than calculating the mod
    (x, y) = extended_euclidean_algo(b, pow(a, 1, b))
    k = a // b
    return (y, x - k * y)


def mod_inverse(a, m):
    """
    Calculates the inverse of a number a modulo m using the extended Euclidean algorithm.
    """
    (x, y) = extended_euclidean_algo(a, m)
    if x < 0:
        x = (x % m + m) % m
    return x


def isPrime(n):
    """
    Check if the number is prime (using sympy to get high performance)
    """
    return sympy.isprime(n)


def factorize_pq(n):
    """
    This function generates two prime numbers, p and q, each with a bit-length of n/2, and returns them as a tuple (p, q). 
    """
    p = random.getrandbits(int(n/2))
    q = random.getrandbits(int(n/2))
    while not isPrime(p):
        p = random.getrandbits(int(n/2))
    while not isPrime(q) or p == q:
        q = random.getrandbits(int(n/2))
    return p, q


def generate_p_q(n_bits):
    """
    This function generates two random prime numbers p and q that are each n_bits long (i.e.,
    between 2**(n_bits-1) and 2**n_bits - 1) using the sympy.randprime function.

    """
    lower_limit = pow(2, n_bits-1)
    upper_limit = pow(2, n_bits) - 1

    p = sympy.randprime(lower_limit, upper_limit)
    q = sympy.randprime(lower_limit, upper_limit)
    while p == q:
        q = sympy.randprime(lower_limit, upper_limit)

    return p, q


p, q = generate_p_q(5)
print(p, q)
p1, q1 = factorize_pq(p*q)
print(p1, q1)
factors = prime_factorization(p*q)
print(factors)
