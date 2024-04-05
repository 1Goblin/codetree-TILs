n, m = tuple(map(int, input().split()))
num = 1

arr2 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        arr2[i][j]=num
        num+=1
        print(arr2[i][j],end=" ")
    print()