import csv

f = open('todos.csv', 'r')
text = csv.reader(f)
print(list(text))
print(list(text[1]))
