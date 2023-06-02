t=int(input())
for i in range(t):
    n=int(input())
    c=0
    for j in range(n):
        a=list(map(int,input().split()))
    for j in range(n):
        if a[j]==0:
            c=c+1
    print(c)
    
