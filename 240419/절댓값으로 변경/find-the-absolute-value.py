n = int(input())
arr = list(map(int,input().split()))

def abvalue(arr, n):
    for i in range(n):
        if arr[i]<0:
            arr[i]*=-1
        
abvalue(arr, n)

for i in arr:
    print(i, end=" ")