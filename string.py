n=int(input())
c=0
for i in range(2,n//2):
    if n%i==0:
        c=1
        break
if n==4 or n==1:
    c=1
print("Yes") if c==0 else print("No")
