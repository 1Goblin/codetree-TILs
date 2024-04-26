n = int(input())
arr = list(map(int, input().split()))
na = []

for i in range(n):
    if i%2==0:
        na = sorted(arr[:i+1])
        print(na[i//2],end=" ")