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

