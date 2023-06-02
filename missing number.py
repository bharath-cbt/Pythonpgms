n=int(input())
for i in range (n):
    a=list(map(int,input().split()))
m=int(input())
for i in range(m):
    b=list(map(int,input().split()))
a.sort()
b.sort()
for i in range(m):
    if b[i] not in a:
        print(b[i])
