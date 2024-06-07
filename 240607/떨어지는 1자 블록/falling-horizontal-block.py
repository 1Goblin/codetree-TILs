n, m, k = tuple(map(int, input().split()))
k -= 1 
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def cant_go(x):
    global k
    for y in range(k,k+m):
        if  x+1 >= n or arr[x+1][y] == 1:
            return True
    return False


for j in range(k,k+m):
    arr[0][j] = 1

for i in range(n):
    if cant_go(i):
        continue
    for j in range(k,k+m):
        arr[i+1][j] = 1
        arr[i][j] = 0


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()