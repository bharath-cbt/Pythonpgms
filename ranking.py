t=int(input())
for i in range(t):
    n=int(input())
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    c=0
    while(fact%10==0):
        c=c+1
        fact=fact/10
    print(c)
