n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

cnt = 0

visited =[
    [False for _ in range(m)]
    for _ in range(n)
]

ans = 0

dxs, dys = [1,0], [0,1]

def in_range(x,y):

    return x>=0 and y>=0 and x<n and y<m

def ok_go(x,y):
    return in_range(x,y) and arr[x][y] == 1 and visited[x][y]


def dfs(x,y):
    dxs, dys = [1,0], [0,1]
    global ans
    
    for dx, dy in zip(dxs,dys):
        ndx, ndy = x+dx, y+dy
        if ok_go(ndx, ndy):
            visited[ndx][ndy] = True
            if ndx==(n-1) and ndy==(m-1):
                cnt = 1
            dfs(ndx, ndy)


print(cnt)