n = int(input())
cnt = 1

arr2 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        arr2[j][i]=cnt
        cnt+=1

for row in arr2:
    for i in row:
        print(i,end=" ")
    print()