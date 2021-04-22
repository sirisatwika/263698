from itertools import permutations
s,n = input().split()
res = ["".join(i) for i in permutations(s,int(n))]
res.sort()
print("\n".join(res))
