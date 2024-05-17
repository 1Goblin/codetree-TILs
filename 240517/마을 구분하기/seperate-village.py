n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

vil_c = 0
vil = []

def ok_go(r,c):
    return r>=0 and c>=0 and r<n and c<n and visited[r][c] == 0 and arr[r][c] == 1


dxs, dys = [1,-1,0,0], [0,0,1,-1]

def dfs(r,c):
    global cnt
    for dx, dy in zip(dxs, dys):
        ndx, ndy = r+dx, c+dy
        if ok_go(ndx,ndy):
            cnt+=1
            visited[ndx][ndy] = 1
            dfs(ndx,ndy)
    return cnt


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and arr[i][j] == 1:
            cnt = 0
            visited[i][j] = 1
            vil.append(dfs(i,j)+1)
            vil_c +=1


print(vil_c)

vil.sort()
for i in vil:
    print(i)