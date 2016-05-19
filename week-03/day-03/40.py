students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

# print(students[1]['name'])
#
#
# for student in students:
#     print(student['age'])
#
# for student in students:
#     if student['age'] < 10:
#         print(student['name'])

num_candies = 0
for student in students:
    if student['age'] < 10:
        num_candies += student['candies']
print(num_candies)


def how_many_candies(list_of_students):
    num_candies = 0
    for student in list_of_students:
        if student['age'] < 10:
            num_candies += student['candies']
    return num_candies

print(how_many_candies(students))
