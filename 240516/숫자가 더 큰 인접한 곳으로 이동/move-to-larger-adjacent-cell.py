n, r, c = tuple(map(int, input().split()))
r -= 1
c -= 1
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def range_in(x,y):
    return x<n and y<n and x>=0 and y>=0

ans = [arr[r][c]]
max_num = arr[r][c]

while (1):
    for dx,dy in zip(dxs, dys):
        ndx, ndy = r+dx, c+dy
        if range_in(ndx, ndy) and arr[ndx][ndy]>max_num:
            r, c = ndx, ndy
            max_num = arr[r][c]
            break
    if ans[-1] == arr[r][c]:
        break
    ans.append(arr[r][c])


for i in ans:
    print(i,end=" ")