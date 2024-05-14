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

di[len(di)-1] //= 2
print(min(di))