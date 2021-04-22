my_list = [1,2,3,4,5,6,7,8,9]
nested_dict = current = {}
for i in my_list:
    current[i] = {}
    current = current[i]
print(nested_dict)