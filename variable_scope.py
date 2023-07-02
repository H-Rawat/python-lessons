name = 'Bro code'  # global variable


def display_name():
    name = 'code'  # local variable
    print(name)  # this will work, but will print local version if present


display_name()
# print(name) --> this will not work
print(name)  # this will print global version
