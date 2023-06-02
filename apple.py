s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
apple=list(map(int,input().rstrip().split()))
orange=list(map(int,input().rstrip().split()))
ap,ora=0,0
for i in apple:
    if i>0 and s<=a+i<=t:
        ap+=1
for j in orange:
    if j<0 and s<=b+j<=t:
        ora+=1
print(ap,ora)
