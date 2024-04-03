import sys

n = int(input())
arr = list(map(int, input().split()))

m = -sys.maxsize
s = []
e =0

while (1):
    for i in range(0,n):
        if arr[i]>m and arr[i] not in s :
            m = arr[i]
        elif arr[i]==m and arr[i] not in s:
            s.oppend(arr[i])
            m = -1
            break 
        if i==n-1:
            e = 1
    if e==1:
        break
print(m)