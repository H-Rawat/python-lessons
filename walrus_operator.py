# assignment expression
# assigns values to variables as part of a larger expression
# new to Python3.8

# happy = True
# print(happy)

# combining above 2 statements together
# print(happy := True)

# example
# foods = list()
# while True:
#     food = input('what food do you like?: ')
#     if food == 'quit':
#         break
#     foods.append(food)

# using walrus
foods = list()
while food := input('what food do you like?: ') != 'quit':
    foods.append(food)
