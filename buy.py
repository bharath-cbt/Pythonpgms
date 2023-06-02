for i in range(int(input())):
    n=input()
    if len(n)%2==0:
        for i in range(len(n)//2):
            if i%2==0:
                print(n[i],end="")
        
