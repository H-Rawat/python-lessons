# used to store multiple items in a single variable

food = ['pizza', 'burger', 'pav bhaji']
food[1] = 'sushi'

food.append('chowmein')
food.remove("sushi")
food.pop()
food.insert(0, 'sushi')
food.sort()
food.clear()

for x in food:
    print(x)
