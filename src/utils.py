import sympy
import random
import key_generation
import time


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
    return nums, len(groups)


def convert_to_string(number):
    """
    Convert a number to the corresponding string back
    """
    string = ''
    char = ''
    while number > 0:
        if (number % 37 in range(0, 10)):
            char = str(number % 37)
        elif (number % 37 in range(10, 36)):
            char = chr(number % 37 + 87)
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
    return pow(a,-1,m)


def isPrime(n):
    """
    Check if the number is prime (using sympy to get high performance)
    """
    return sympy.isprime(n)


def generate_pq_bybits(n):
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


def receiving_setup(receiver, socket):
    """
    The receiving_setup function sets up the receiver's public key by generating two prime numbers p and q of length n_bits using generate_p_q function, and then generating the public key e using generate_e function from key_generation module. Finally, it sends the public key to the sender through the given socket by encoding it as a string.
    """
    n_bits = 10
    print("Generating p,q of length: "+str(n_bits)+" bits")
    p, q = generate_p_q(n_bits)
    print("p: ", p, " q: ", q)

    e = key_generation.generate_e((p-1)*(q-1))
    receiver.initialize_public_key(p, q, e)

    print("Sending the public key")
    public_key = str(e)+" "+str(p*q)
    print("Public key "+public_key)
    socket.send(str(public_key).encode())


def sending_setup(sender, socket):
    """
    This function sets up the public key for the sender by receiving the public key from the receiver over the provided socket connection. It decodes the public key and initializes the sender's public key with the provided values of 'e' and 'n'.
    """
    print("Recieving the public key")
    public_key = socket.recv(1024).decode()
    public_key = public_key.split(" ")
    e = int(public_key[0])
    n = int(public_key[1])
    print("Recieved: "+str(e)+" "+str(n))
    sender.initialize_public_key(e, n)


def send_message(sender, socket):
    """
    This function prompts the user to enter a message, encrypts it , and sends the encrypted message over a socket connection. It then prints the response received from the receiver.
    """
    message = input("Entered the message: ")
    splited = split_message(message)
    m, count = convert_to_number(splited)
    socket.send(str(count).encode())
    for i in m:
        ciphertext = sender.encryption(i)
        print("Encrypted: " + str(ciphertext))
        socket.send(str(ciphertext).encode())
        time.sleep(0.01)
    print(socket.recv(1024).decode())


def receive_message(receiver, socket):
    """
    This function receives an encrypted message through a socket connection, decrypts it using the provided receiver object, and prints the decrypted message. Then, it sends an acknowledgement message through the socket to notify the sender that the decryption is done.
    """
    print("Receiving message")
    count = int(socket.recv(1024).decode())
    full_plaintext = ""
    while count > 0:
        ciphertext = socket.recv(1024).decode()
        print("ciphertext received: "+ciphertext)
        plaintext = receiver.decryption(ciphertext)
        full_plaintext = full_plaintext + plaintext
        count = count-1
    print("Originial message from sender: " + full_plaintext)
    socket.send(str("Done decryption").encode())
