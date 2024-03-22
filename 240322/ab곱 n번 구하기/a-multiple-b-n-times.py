n = int(input())

for i in range(n):
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    num = 1
    for j in range(a, b+1):
        num*=j
    print(num)