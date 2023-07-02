# packs all arguments into a tuple
# useful in case a function should accept a varying amount of arguments
# asterisk is important, you can any name after the *

def add(*args):
    sum = 0
    # to cast a tuple to a list to make it mutable
    # args = list(args)
    # args[1] = 0
    for i in args:
        sum += i
    return sum


print(add(1, 1, 1, 1, 1, 1, 1, 1, 1))
