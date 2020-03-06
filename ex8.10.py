# a string slice can take a third index that specifies the 'step size'
# the number of spaced between successive characters
# 2 means every other character
# 3 means every third

# fruit = 'banana'
# print(fruit[0:5:2])

def is_palindrome(string):
    print(string == string[::-1])

is_palindrome('racecar')
is_palindrome('apple')
