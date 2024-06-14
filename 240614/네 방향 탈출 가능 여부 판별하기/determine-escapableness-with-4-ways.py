# from collections import deque

# n, m = tuple(map(int, input().split()))

# arr = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# visited = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

# q = deque()

# dxs, dys = [-1,1,0,0], [0,0,-1,1]

# def ok_go(r,c):
#     return r>=0 and c>=0 and r<n and c<m and arr[r][c] == 1 and visited[r][c] == 0


# def bfs():
#     while q:
#         r, c = q.popleft()
#         for dx, dy in zip(dxs, dys):
#             ndx, ndy = r+dx, c+dy
#             if ok_go(ndx,ndy):
#                 visited[ndx][ndy] = 1
#                 arr[ndx][ndy] = 2
#                 q.append((ndx,ndy))

# q.append((0,0))
# bfs()


# if arr[-1][-1] == 2:
#     print(1)
# else:
#     print(0)

from collections import deque

n, m = tuple(map(int, input().split()))

arr = [
    list(map(int ,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

q = deque()

def can_go(x, y):
    return x>=0 and y>=0 and x<n and y<m and visited[x][y] == 0


dxs, dys = [1,-1,0,0], [0,0,1,-1]


def bfs():
    while q:
        r,c = q.popleft()

        for dx, dy in zip(dxs, dys):
            n_dx, n_dy = r+dx, c+dy
            if can_go(n_dx,n_dy):
                visited[n_dx][n_dy] = 1
                q.append((n_dx,n_dy))

q.append((0,0))
bfs()

if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)