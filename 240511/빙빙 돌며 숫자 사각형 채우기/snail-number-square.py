n, m = tuple(map(int, input().split()))
x,y = 0,0
dir_num = 0

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

arr[0][0]=1

dx,dy = [0,1,0,-1], [1,0,-1,0]

def in_range(nx,ny):
    return  0<=nx and 0<=ny and nx<n and ny<m


for i in range(2,n*m+1):

    nx, ny = x+dx[dir_num], y+dy[dir_num]

    if not in_range(nx,ny) or arr[nx][ny] != 0:
        dir_num = (dir_num+1)%4
    
    x, y = x+dx[dir_num], y+dy[dir_num]

    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()