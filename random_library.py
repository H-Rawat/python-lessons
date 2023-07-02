import random

x = random.randint(1, 6)

# random float number between 0 and 1
y = random.random()

# to choose a random thing from a list
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

# shuffle
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)

# print(x)
# print(y)
# print(z)
print(cards)
