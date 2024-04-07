n = int(input())

arr2 =[
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    arr2[i][0] = 1

for i in range(1, n):
    for j in range(1,n):
        arr2[i][j] = arr2[i-1][j-1] + arr2[i-1][j]


for row in arr2:
    for i in row:
        if i!=0:
            print(i,end=" ")
    print()