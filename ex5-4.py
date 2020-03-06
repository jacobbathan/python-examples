def is_triangle(a,b,c):
    if a > (b+c) or b > (a+c) or c > (a+b):
        print('No')
    else:
        print('Yes')


# is_triangle(3, 4, 5)
def triangle_inputs():
    length1 = int(input('What is the first value? '))
    length2 = int(input('What is the second value? '))
    length3 = int(input('What is the third value? '))

    is_triangle(length1, length2, length3)

triangle_inputs()
