n, m = tuple(map(int, input().split()))
num = 0

arr2 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(m):
    if i%2==0:
        for j in range(n):
            arr2[j][i]=num
            num+=1
    else:
        for k in range(n-1,-1,-1):
            arr2[k][i]=num
            num+=1


for row in arr2:
    for j in row:
        print(j,end=" ")
    print()