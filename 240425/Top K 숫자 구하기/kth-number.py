n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()

for i in range(n):
    if i==(k-1):
        print(arr[i])