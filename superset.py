a = set(input().split())
t = int(input())
cnt = 0
for i in range(t):
    b = set(input().split())
    if(a.issuperset(b)):
        cnt = cnt + 1
print(cnt == t)
