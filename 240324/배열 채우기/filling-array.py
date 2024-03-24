arr = list(map(int,input().split()))
a = []
c=0
for i in arr:
    if i==0:
        break
    a.append(i)
    c+=1
b = a[::-1]

for k in b:
    print(k,end=" ")