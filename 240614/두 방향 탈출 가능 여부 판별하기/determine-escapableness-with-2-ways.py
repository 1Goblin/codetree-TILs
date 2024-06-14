# n, m = tuple(map(int, input().split()))

# arr = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# cnt = 0

# visited =[
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

# ans = 0

# dxs, dys = [1,0], [0,1]

# def in_range(x,y):

#     return x>=0 and y>=0 and x<n and y<m

# def ok_go(x,y):
#     return in_range(x,y) and arr[x][y] == 1 and not visited[x][y]


# def dfs(x,y):
#     dxs, dys = [1,0], [0,1]
#     global cnt
    
#     for dx, dy in zip(dxs,dys):
#         ndx, ndy = x+dx, y+dy
#         if ok_go(ndx, ndy):
#             visited[ndx][ndy] = 1
#             dfs(ndx, ndy)
#             if ndx==(n-1) and ndy==(m-1):
#                 cnt = 1

# dfs(0,0)

# print(cnt)
    

n, m = tuple(map(int, input().split()))

ans = 0

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [1,0], [0,1]


def can_go(x,y):
    return x>=0 and y>=0 and x<n and y<m and arr[x][y] != 0


def dfs(x, y):
    global ans
    for dx,dy in zip(dxs, dys):
        n_dx, n_dy = x+dx, y+dy
        if can_go(n_dx, n_dy):
            if n_dx == n-1 and n_dy == m-1:
                ans = 1
            dfs(n_dx, n_dy)

dfs(0,0)

print(ans)