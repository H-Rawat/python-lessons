# Python Lessons

- Strings cant be used for any kind of math, you will have to use a numeric data type for that.

```
print("age " + age)
```

This will give an error saying "cant concatenate str with int"

**Solution**

```
print("age " + str(age))
```

## STRING METHODS

`variable_name.capitalize()` - Makes the first letter of the string capital and the rest lowercase.

`isalpha()` - return true for strings like these 'brocode', but for strings with any space it returns false.
