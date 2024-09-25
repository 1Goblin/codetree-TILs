n, m = tuple(map(int, input().split()))

ndx, ndy = [0,0,1,-1], [1,-1,0,0]

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def isRange(r, c):
    return r>=0 and r<n and c>=0 and c<n

for i in range(m):
    r, c = tuple(map(int, input().split()))
    r-=1
    c-=1
    arr[r][c] = 1

    count = 0 
    for dx, dy in zip(ndx,ndy):
        dxs =r + ndx[dx]
        dys =c + ndy[dy]


        if not isRange(dxs, dys):
            continue
            
        if arr[dxs][dys] == 1:
            count+=1
            
 
    if count >= 3:
        print(1)
    else:
        print(0)