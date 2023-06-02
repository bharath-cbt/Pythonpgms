# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().rstrip().split()))
    m=int(input())
    b=list(map(int,input().rstrip().split()))
    c=0
    for i in b:
        if i not in a:
            c=0
            break
        else:
            c=c+1
    if c!=0:
        print("Yes")
    else:
        print("No")
    
            
