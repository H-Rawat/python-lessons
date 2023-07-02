try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print('this will always run')
