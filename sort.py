# SORT for lists
# students = ['squidward', 'sandy', 'patrick', 'spongebob']

# students.sort(reverse=True)

# for i in students:
#     print(i)

# SORT function for iterables
# students = ('squidward', 'sandy', 'patrick', 'spongebob')

# sorted_students = sorted(students, reverse=True)  # returns a list

# for i in sorted_students:
#     print(i)

students = (
    ('Squidward', "f", 60),
    ('Sandy', "A", 33),
    ('Patrick', "D", 20),
    ('Spongebob', "B", 70),
)

# to sort by 1st col
# students.sort()

# to sort by 2nd col
# grade = lambda grades:grades[1]
# students.sort(key=grade)

# to sort by 3rd col
age = lambda ages:ages[2]
# students.sort(key=age)
sorted_students = sorted(students, key=age)

for i in students:
    print(i)
