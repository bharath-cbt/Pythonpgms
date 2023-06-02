# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if x*3<=y else print("NO")
