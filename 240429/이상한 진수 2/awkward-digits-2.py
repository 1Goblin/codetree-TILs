arr = list(map(int,input()))

for i in range(1,len(arr)):
    if arr[i]==0:
        arr[i] = 1
        break

arrlen = len(arr)-1

result = 0
for i in arr:
    if i==1:
        result += 2**arrlen
        arrlen-=1

print(result)