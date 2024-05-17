from collections import deque

n, k = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def can_go(r,c):
    return r>=0 and c>=0 and r<n and c<n and visited[r][c] == 0 and arr[r][c] == 0

def bfs():
    while q:
        r, c = q.popleft()
        for dx, dy in zip(dxs,dys):
            ndx, ndy = r+dx, c+dy
            if can_go(ndx,ndy):
                visited[ndx][ndy] = 1
                q.append((ndx,ndy))

for _ in range(k):

    q = deque()
    r,c = tuple(map(int, input().split()))
    r -=1
    c -=1
    if can_go(r,c):
        visited[r][c] = 1
        q.append((r,c))
        bfs()
ans = 0

for i in range(n):
    for j in range(n):
        ans+=visited[i][j]

print(ans)