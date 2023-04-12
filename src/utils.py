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
