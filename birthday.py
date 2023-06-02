'''candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
c=max(candles)
l=0
#print(c)
for i in candles:
    if i==c:
        l=l+1
print(l)'''

'''candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
c=0
for i in candles:
    if i==max(candles):
            c=c+1
print(c)
'''

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
candles.sort(reverse=True)
c=0
for i in candles:
    if i==max(candles):
            c=c+1
    else:
        break
print(c)
