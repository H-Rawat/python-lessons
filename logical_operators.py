temp = int(input('what is the temperature outside? '))

if not (temp > 0 and temp < 30):
    print('ok')
elif temp < 0 or temp > 30:
    print('bad temp')
    print('stay inside')
