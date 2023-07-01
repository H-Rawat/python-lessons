# break -> to terminate the loop entirely
# -----

while True:
    name = input('Enter your name: ')
    if name != "":
        break

# continue -> skips to next iteration of the loop
# --------

phone_num = '123-456'

for i in phone_num:
    if i == '-':
        continue
    print(i, end="")

# pass -> does nothing, acts as a placeholder
# ----

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
