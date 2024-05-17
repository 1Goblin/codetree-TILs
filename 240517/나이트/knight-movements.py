from collections import deque

n = int(input())

r1, c1, r2, c2 = tuple(map(int, input().split()))
r1-=1
c1-=1
r2-=1
c2-=1

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

q = deque()

dxs, dys = [-1,-2,-2,-1,1,2,2,1],[-2,-1,1,2,2,1,-1,-2]


def can_go(r,c):
    return  r>=0 and c>=0 and r<n and c<n and visited[r][c] == 0

def bfs():
    while q:
        r,c = q.popleft()
        for dx,dy in zip(dxs,dys):
            ndx, ndy = r+dx, c+dy
            if can_go(ndx,ndy):
                step[ndx][ndy] = step[r][c]+1
                visited[ndx][ndy] = 1
                q.append((ndx,ndy))

q.append(((r1),(c1)))
bfs()

print(step[r2][c2] if step[r2][c2] !=0 else -1)