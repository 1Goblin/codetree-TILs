import sys

n = int(input())
arr = list(map(int, input().split()))

fm = arr[0]
tm = arr[0]
m = 0

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]<arr[j+1]:
            m = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = m
print(arr[0], arr[1])