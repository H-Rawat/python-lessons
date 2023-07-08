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

---

## STRING METHODS

`variable_name.capitalize()` - Makes the first letter of the string capital and the rest lowercase.

`isalpha()` - return true for strings like these 'brocode', but for strings with any space it returns false.

---

**By default, the data-type returned from the `input()` function is a string.**

**If we cast a string to an integer, it can only be a whole number.**

---

`abs()` tells you how far a number is from 0. Also can be used to convert -ve numbers to +ve numbers

---

`while` loop could execute unlimited amount of times.  
With `for` loop, we know the amount of times we want the code to execute.

---

add `end=''` in the print statement to avoid the print statement showing the next print in the next line.  
`print('hello', end='')`

---

If a function in python returns nothing then it return `None`.
