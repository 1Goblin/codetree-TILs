n = int(input())
arr = list(map(int, input().split()))

def evendiv(arr, n):
    for i in range(n):
        if arr[i]%2==0:
            arr[i] = arr[i]//2

evendiv(arr, n)

for i in arr:
    print(i,end=" ")