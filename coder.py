t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=pow(a,b)
    print(c%10)
