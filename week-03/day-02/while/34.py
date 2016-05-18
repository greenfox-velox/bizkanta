ag = [3, 4, 5, 6, 7]
# please double all the elements of the list

i = 0

while i < len(ag):
  ag[i] *= 2
  i += 1
print(ag)

j = 0
lenag = len(ag)

while j < lenag:
    print(ag[j])
    ag += [ag[j]]
    j += 1
print(ag)
