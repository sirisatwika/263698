my_list = []
n = int(input("enter no of elements : "))
for i in range(1, n+1):
    x = int(input("element : "))
    my_list.append(x)
my_list.sort()
print(my_list[-2])
