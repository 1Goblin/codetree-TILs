arr = list(map(int, input().split()))

arr.sort()


if arr[2] == arr[0]+arr[1]:
    c = arr[3]
else:
    c = arr[2]

print(arr[0], arr[1], c)