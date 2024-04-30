n = int(input())
tcnt = 0

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1, 0 ,-1]
dys = [1, 0 ,-1, 0]

def ran(x, y):
    return x >= 0 and  y >= 0 and x < n and y < n


for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if ran(nx, ny) and arr[nx][ny] == 1:
                cnt +=1
        if cnt>=3:
            tcnt+=1


print(tcnt)