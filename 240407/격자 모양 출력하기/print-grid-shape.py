n, m = tuple(map(int, input().split()))

arr2 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    a, b = tuple(map(int, input().split()))
    arr2[a-1][b-1] = a*b

for row in arr2:
    for i in row:
        print(i,end=" ")
    print()