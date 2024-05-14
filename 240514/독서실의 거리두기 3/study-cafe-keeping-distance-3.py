n = int(input())
arr= input()
arr = list(map(int, arr))

di = []

d = 0

for i in range(1,len(arr)):
    if arr[i]==1:
        di.append(i-d)
        d = i

di.sort()

if di[len(di)-1]%2==0:
    di[len(di)-1] //= 2
else:
    di[len(di)-1] = di[len(di)-1]//2 + 1

print(min(di))