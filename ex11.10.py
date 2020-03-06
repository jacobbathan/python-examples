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

    return new_string

def make_dictionary(file):
    word_dictionary = {}
    wordlist = open(file)
    for line in wordlist:
        word = line.strip().lower()
        word_dict[word] = []
    return word_dict

def find_rotate_pairs(dictionary):
    rotate_pairs = []
    for item in dictionary:
        for num in range(1, 26):
            rotate = rorate_word(item, num)
            if rotate in dictionary:
                rotate_pairs += ['rotation: ' + str(num) + item + ' / ' + rotate]
    return rotate_pairs            
