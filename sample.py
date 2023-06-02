for i in range(int(input())):
    n,m=map(int,input().split())
    if n>=m:
        print(0)
        continue
    c=0
    while m>n:
       c+=1
       n+=8
    print(c)
        
