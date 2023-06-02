for i in range(int(input())):
    n=input()
    if n[-1]=="x" or n[-1]=="s" or n[-1]=="o" or (n[-2]=="c" and n[-1]=="h"):
        for j in range(len(n)):
            print(n[j],end="")
        print("es",end="")
    elif n[-1]=="f" or (n[-2]=="f" and n[-1]=="e"):
        j=0
        while(n[j]!="f"):
            print(n[j],end="")
            j+=1
        print("ves",end="")
    elif n[-1]=="y":
        j=0
        while(n[j]!="y"):
            print(n[j],end="")
            j+=1
        print("ies",end="")
    else:
        print(n,end="")
        print("s",end="")
    print("")
        
                                    
