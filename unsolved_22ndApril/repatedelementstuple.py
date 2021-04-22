tup = (1 , 2, 3, 3, 4, 2, 1, 5, 1, 2, 4, 7)
unique = list(set(tup))
rep = []
for i in unique:
    if tup.count(i) > 1:
        rep.append(i)
print(rep)