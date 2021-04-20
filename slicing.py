list_1 = [1]
list_2 = list_1[:] # Copy the entire list.
list_1[0] = 2
print(list_2)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] #copy some part of list
print(new_list)
new_list = my_list[1:-1]
print(new_list)
new_list = my_list[:3]
print(new_list)