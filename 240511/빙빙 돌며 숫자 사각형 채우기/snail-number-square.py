n, m = tuple(map(int, input().split()))
x,y = 0,0
dir_num = 0

cnt = 1

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

arr[0][0]=1

dx,dy = [0,1,0,-1], [1,0,-1,0]

def in_range(nx,ny):
    return  0<=nx and 0<=ny and nx<n and ny<m

check = 0
while(1):

    nx, ny = x+dx[dir_num], y+dy[dir_num]

    if in_range(nx,ny) and arr[nx][ny] == 0:
        cnt+=1
        x, y = nx, ny
        arr[x][y] = cnt
        check = 0
    else:
        check+=1
        if check>=2:
            break
        dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()