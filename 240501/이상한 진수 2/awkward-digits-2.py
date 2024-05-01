n = list(map(int, input()))

result = 0
for i in range(len(n)):
    if n[i]==0:
        n[i] = 1
        break

if len(n)==1 and n[0]==1:
    n[0] = 0

l = len(n) -1
for j in range(len(n)):
    result+=n[j]*2**l
    l-=1



print(result)