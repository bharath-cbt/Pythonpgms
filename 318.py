def checkPrime(num):
    if num < 2:
        return 0
    else:
        x = num // 2
        for j in range(2, x + 1):
            if num % j == 0:
                return 0
    return 1
t=int(input())
for i in range(t):
    m,n=map(int,input().split());
    for i in range(m, n + 1):
        if checkPrime(i):
            print(i)

