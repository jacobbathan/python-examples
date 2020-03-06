import math

def test_square_root(a):
    squareroot1 = my_square_root(a)
    squareroot2 = get_sqrt(a)
    absolute_difference = squareroot1 - squareroot2
    print(str(a) + ' | ' + str(squareroot1) + ' | ' + str(squareroot2) + ' | ' + str(absolute_difference))

def my_square_root(a):
    x = a/2
    while True:
        root = (x + a/x) / 2
        if root == x:
            return root
        x = root

def get_sqrt(x):
    return math.sqrt(x)
    
test_square_root(16012041531)
