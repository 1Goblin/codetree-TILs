n = int(input())
arr = list(map(int, input().split()))
na = []

def mid(ar,n):
    return ar[n//2]

for i in range(n):
    na.append(arr[i])
    if i%2==0:
        na.sort()
        print(na[i//2],end=" ")