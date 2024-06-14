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

# seq = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

# q = deque()

# def ok_go(r, c):
#     return r>=0 and c>=0 and r<n and c<m and visited[r][c] == 0 and arr[r][c] == 1


# def bfs():
#     dxs, dys = [1,-1,0,0], [0,0,1,-1]
#     while q:
#         r, c = q.popleft()
#         for dx, dy in zip(dxs,dys):
#             ndx, ndy = r+dx, c+dy
#             if ok_go(ndx, ndy):
#                 seq[ndx][ndy] = seq[r][c]+1
#                 visited[ndx][ndy] = 1
#                 q.append((ndx,ndy))


# q.append((0,0))
# visited[0][0] = 1
# bfs()

# # for i in range(n):
# #     for j in range(m):
# #         print(seq[i][j],end=" ")
# #     print()

# print(seq[-1][-1] if seq[-1][-1] != 0 else -1)

from collections import deque

n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(m)
]

seq = [
    [0 for _ in range(m)]
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def can_go(x,y):
    return x>=0 and y>=0 and x<n and y<m and  visited[x][y] == 0 and arr[x][y] == 1


q = deque()


def bfs():
    dxs, dys = [1,-1,0,0], [0,0,1,-1]
    while q:
        r, c = q.popleft()
        for dx, dy in zip(dxs, dys):
            ndx, ndy = r+dx, c+dy
            if can_go(ndx, ndy):
                seq[ndx][ndy] = seq[r][c] + 1
                visited[ndx][ndy] = 1
                q.append((ndx,ndy))


q.append((0,0))
visited[0][0] = 1
bfs()


print(seq[-1][-1] if seq[-1][-1] != 0 else -1)