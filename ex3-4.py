def do_twice(function, value):
    function(value)
    function(value)

def print_twice(string):
    print(string)
    print(string)

do_twice(print_twice, 'spam')

def do_four(function, value):
    do_twice(function, value)
    do_twice(function, value)

do_four(print_twice, 'spam')
    
