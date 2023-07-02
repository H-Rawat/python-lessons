# more control when displaying output

# animal = 'cow'
# item = 'moon'

# print('the ' + animal + ' jumped over the ' + item)
# print("The {} jumped over the {}".format(animal, item))

# {} -> format fields

# positional argument
# print("The {1} jumped over the {0}".format(animal, item))

# keyword argument
# print("The {animal} jumped over the {item}".format(animal='cow', item='moon'))

# using format arguments multiple times
# print("The {animal} jumped over the {animal}".format(
#     animal='cow', item='moon'))

# more elegant way
# text = 'The {} jumped over the {}'
# print(text.format(animal, item))

# adding padding
# name = 'bro'

# print('hello, my name is {:10}. Nice to meet you'.format(name))

# left align
# print('hello, my name is {:<10}. Nice to meet you'.format(name))

# right align
# print('hello, my name is {:>10}. Nice to meet you'.format(name))

# center
# print('hello, my name is {:^10}. Nice to meet you'.format(name))

# print('hello, my name is {name:^10}. Nice to meet you'.format(name='messi'))

# Format numbers
# number = 1000

# print('the number pi is {:.2f}'.format(number))
# print('the number pi is {:,}'.format(number))

# binary
# print('the number pi is {:b}'.format(number))

# octal
# print('the number pi is {:o}'.format(number))

# hexadecimal
# print('the number pi is {:x}'.format(number))
# print('the number pi is {:X}'.format(number))

# print('the number pi is {:e}'.format(number))
# print('the number pi is {:E}'.format(number))
