# way to create new list with less syntax
# easier to read
# list = [expression (if/else) for item in iterable]

# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)

# squares = [i * i for i in range(1, 11)]
# print(squares)

# TO MIMIC CERTAIN LAMBDA FUNCTIONS
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
# passed_students = list(filter(lambda x: x >= 60, students))
# print(passed_students)

# USING LIST COMPREHENSION
print([g for g in students if g >= 60])
print([g if g >= 60 else 'failed' for g in students])