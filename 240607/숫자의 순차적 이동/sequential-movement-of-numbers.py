n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs,dys = [1,1,1,-1,-1,-1,0,0], [1,-1,0,1,-1,0,1,-1]


def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

def find_num(num):
    
    for x in range(n):
        for y in range(n):
            if arr[x][y] == num:
                return x, y


def swap(r1,c1,r2,c2):

    temp = arr[r1][c1]
    arr[r1][c1] = arr[r2][c2]
    arr[r2][c2] = temp
    

for _ in range(m):
    for p in range(1,17):

        i, j = find_num(p)

        maxV = 0
        maxP = (-1,-1)

        for dx, dy in zip(dxs,dys):
            ndx, ndy = i+dx, j+dy
            if in_range(ndx, ndy) and arr[ndx][ndy] > maxV:
                maxV = arr[ndx][ndy]
                maxP = (ndx,ndy)
        
        r,c = maxP
        swap(i,j,r,c)


for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()