name = 'Bro Code'

first_name = name[0:3]
first_name = name[:3]
last_name = name[4:]
funky_name = name[::3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# SLICE
# -----
website1 = 'htpp://twitter.com'
website2 = 'htpp://reddit.com'
website3 = 'htpp://discord.com'

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
print(website3[slice])
