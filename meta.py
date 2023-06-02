for i in range(int(input())):
    x,n,m=map(int,input().split())
    for j in range(n):
        x=pow(x,x)
    print(x%m)
