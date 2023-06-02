# cook your dish here
t=int(input())
if 1<=t and t<=1000:
    for i in range(t):
        n=int(input())
        s=1
        if 0<=n and n<=20:
            for i in range(1,n+1):
                s=s*i
        print(s)
            
