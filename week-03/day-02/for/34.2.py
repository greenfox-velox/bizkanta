ag = [3, 4, 5, 6, 7]
# please double all the elements of the list
#
# for i in range(len(ag)):
#     ag[i] *= 2
# print(ag)


lenag = len(ag)

for j in range(lenag):
    ag += [ag[j]]
print(ag)
