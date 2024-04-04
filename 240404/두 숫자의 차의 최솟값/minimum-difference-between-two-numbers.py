import sys

n = int(input())
arr = list(map(int, input().split()))

m = sys.maxsize

for i in range(n-1):
    if arr[i+1]-arr[i]<m:
        m = arr[i+1]-arr[i]
print(m)