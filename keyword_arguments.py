# arguments preceded by an identifier when we pass them to a function.
# The order of the arguments does not matter, unlike positional arguments python knows the names of the arguments that our function receives

# POSITION ARGUMENTS - the order of arguments matter
def hello(first, middle, last):
    print('hello', first, middle, last)


# hello('bro', 'code', 'dude')

# KEYWORD ARGUMENTS
hello(middle='bro', last='code', first='dude')
