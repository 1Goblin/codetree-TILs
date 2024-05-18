n, m, t = tuple(map(int, input().split()))

cnt = 0

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [0,0,1,-1], [1,-1,0,0]


for i in range(m):
    r, c = tuple(map(int, input().split()))
    count[r-1][c-1] = 1


def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

def delete():
    for i in range(n):
        for j in range(n):
            if ncount[i][j] > 1:
                ncount[i][j] = 0


def move(r,c):
    max_num = 0
    max_pos = (-1,-1)
    for dx, dy in zip(dxs, dys):
        ndx, ndy = r+dx, c+dy
        if in_range(ndx,ndy) and arr[ndx][ndy] >= max_num:
            max_num = arr[ndx][ndy]
            max_pos = (ndx,ndy)
    r,c = max_pos
    ncount[r][c] += 1 

for _ in range(t):
    ncount = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i,j)
    delete()
    count = ncount
            
for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            cnt+=1

print(cnt)