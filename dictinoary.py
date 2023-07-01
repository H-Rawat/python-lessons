# changeable, unorderd collection of unique key:value pairs.
# Fast because they use hashing, allows us to access a value quickly

capitals = {
    'usa': 'washington dc',
    'china': 'beijing',
    'india': 'delhi'
}

capitals.update({'germany': 'berlin'})
capitals.update({'usa': 'california'})
capitals.pop('china')
capitals.clear()

print(capitals['usa'])

much safer way to access a key is to use get() method
print(capitals.get('germany'))
print(capitals.get('india'))

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, ' -> ', value)
