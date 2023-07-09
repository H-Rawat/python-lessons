# function that either: accepts a func as arg or returns a func
# functions are treated as objects in python

# def loud(text):
#     return text.upper()


# def quite(text):
#     return text.lower()


# def hello(func):
#     text = func('Hello')
#     print(text)


# hello(loud)
# hello(quite)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))
