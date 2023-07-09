# applies a function to an iterable and reduce it to a single cumulative value.
# perform the function on first 2 values and repeats the process until 1 value remains

import functools

# letters = ['H', 'E', 'L', 'L', 'O']

# word = functools.reduce(lambda x, y: x + y, letters)
# print(word)

factorial = [5, 4, 3, 2, 1]
print(functools.reduce(lambda x, y: x * y, factorial))