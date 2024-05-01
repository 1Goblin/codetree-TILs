n = list(map(int, input()))

result = 0
for i in range(len(n)):
    if n[i]==0:
        n[i] = 1
        break
    if i==len(n)-1:
        n[i]=0

l = len(n) -1
for j in range(len(n)):
    result+=n[j]*2**l
    l-=1



print(result)