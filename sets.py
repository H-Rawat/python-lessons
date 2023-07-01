# unordered, unindexed, and no duplicate values

utensils = {
    'fork',
    'spoon',
    'knife',
}

dishes = {
    'bowl',
    'plate',
    'cup',
    'knife'
}

utensils.add('napkin')
utensils.remove('napkin')
utensils.clear()
utensils.update(dishes)
dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)

print(dishes.difference(utensils))
print(dishes.intersection(utensils))
