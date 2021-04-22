my_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6)]
my_dictionary = {}
for i,j in my_list:
    my_dictionary.setdefault(i, []).append(j)
print(my_dictionary)

l = [("a",1),("b",2),("c",3),("a",2),("b",2),("c",3)]
d = {}
for i,j in l:
    d.setdefault(i, []).append(j)
print(d)
