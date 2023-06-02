for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().rstrip().split()))
    a.sort()
    for j in range(len(a)-1):
        if a[j+1]-a[j]<=1:
            a.pop(j)
    print("YES") if len(a)!=1 else print("NO")
        
               
