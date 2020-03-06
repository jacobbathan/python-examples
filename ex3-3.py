def right_justify(s):
    length = len(s)
    spaces = 70 - length
    print((" " * spaces) + s)

right_justify('allen')
