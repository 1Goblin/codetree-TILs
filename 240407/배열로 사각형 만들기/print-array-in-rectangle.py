arr2 = [
    [0 for _ in range(5)]
    for _ in range(5)
]


for i in range(5):
    arr2[0][i] = 1
    arr2[i][0] = 1

for i in range(1,5):
    for j in range(1,5):
        arr2[i][j] = arr2[i-1][j] + arr2[i][j-1]

for row in arr2:
    for i in row:
        print(i,end=" ")
    print()