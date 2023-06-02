def prec(c):
    if c=='^':
        return 3
    elif c=='*' or c=='/':
        return 2
    elif c=='+' or c=='-':
        return 1
    else :
        return 0
    
t=int(input())
if t<=100:
    for i in range(t):
        n=input()
        arr=[]
        temp=[]
        for j in n:
            if j=="(":
                temp.append(j)
            elif j.isalpha():
                arr.append(j)
            elif j==")":
                while(temp[-1]!="("):
                    arr.append(temp[-1])
                    temp.pop()
            else:
                while prec(j)<=prec(temp[-1]):
                    if n[j]=="^" and temp[-1]=="^":
                        break
                    else:
                        x=temp[-1]
                        temp.pop()
                        arr.append(x)
                temp.append(j)
        for j in temp:
            if j=="(":
                temp.remove(j)
        while len(temp)!=0:
            x=temp[-1]
            temp.pop()
            arr.append(x)
        for j in arr:
            print(j,end="")
        del arr
        del temp
                
    
