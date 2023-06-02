# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print("YES") if n*5>=m else print("NO")
