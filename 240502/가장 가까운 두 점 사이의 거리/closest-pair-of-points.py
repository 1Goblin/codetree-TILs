import sys

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_d = sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        x = (arr[i][0] - arr[j][0]) **2
        y = (arr[i][1] - arr[j][1]) **2
        d = x+y
        min_d = min(d, min_d)

print(min_d)