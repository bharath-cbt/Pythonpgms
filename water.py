n=input()
c=0
for i in range(len(n)):
    if n[i].isupper():
        c+=1
if c>len(n)//2:
    print(n.upper())
else:
    print(n.lower())
