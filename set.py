# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
words = [list(map(str, input().split())) for _ in range(n)]
words_occurences={}
for word in words:
    words_occurences[word]=0
for word in words:   
    words_occurences[word]+=1  
print(len(words_occurences))
occurences=words_occurences.values()
for i in occurences:
    print(i,end=" ")

