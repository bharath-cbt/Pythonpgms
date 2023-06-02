n=int(input())
if 1<=n and n<=100:
    a=list(map(int,input().rstrip().split()))
b=[]
a.sort(reverse=True)
for i in a:
    if sum(b)<=(sum(a))/2:
        b.append(i)
print(len(b))
    
    

