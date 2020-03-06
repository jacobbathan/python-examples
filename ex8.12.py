# exercise 8.12 ROT13 encryption

def rotate_word(string, rotations):
    lower_string = string.lower()
    num_string = []
    new_string = ''

    for char in lower_string:
        num_char = ord(char) - 96 + rotations
        num_string.append(num_char)

    for num in num_string:
        new_char = chr(96 + (num % 26))
        new_string += new_char

    print(new_string)

rotate_word('cheer',7) # expeceted result: jolly
rotate_word('melon', -10) # expected result: cubed
