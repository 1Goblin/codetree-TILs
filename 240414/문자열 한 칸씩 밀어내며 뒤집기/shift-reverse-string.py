a = input().split()
arr = a[0]
n = int(a[1])

for _ in range(n):
    a = int(input())
    if a==1:
        arr = arr[1:] + arr[0]
        print(arr)
    elif a==2:
        arr = arr[-1] + arr[:-1]
        print(arr)
    elif a==3:
        arr = arr[::-1]
        print(arr)