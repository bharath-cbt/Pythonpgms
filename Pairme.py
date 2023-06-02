n=int(input())
for i in range(n):
    x,y,z=map(int,input().split())
    if (x==y+z) or (y==x+z) or (z==y+x):
        print('YES')
    else:
        print('NO')
