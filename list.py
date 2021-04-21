t = int(input())
arr = []
n1 = 0
n2 = 0
for i in range(t):
    lis = input()
    lis = lis.split()
    if lis[0] == "insert":
        n1 = int(lis[1])
        n2 = int(lis[2])
        arr.insert(n1,n2)
    elif lis[0] == "print":
        print(arr)
    elif lis[0] == "remove":
        n1 = int(lis[1])
        arr.remove(n1)
    elif lis[0] == "append":
        n1 = int(lis[1])
        arr.append(n1)
    elif lis[0] == "sort":
        arr.sort()
    elif lis[0] == "pop":
        arr.pop()
    elif lis[0] == "reverse":
        arr.reverse()
