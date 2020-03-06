# write function named uses_only that takes a word and a string of letters
# returns true if word contains only lettters in the list

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True


print(uses_only('apple', 'pie')) # returns false
print(uses_only('banana', 'ban')) # returns true


