n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(m)]  # m개의 0을 가진 리스트를 생성
    for _ in range(n)       # n번 반복하여 위 리스트를 만듦
]

dxs, dys = [0,1,0,-1], [1,0,-1,0]
x,y=0,0

def isRange(x,y):
    return x>=0 and x<n and y>=0 and y<m

def isFill(dx,dy):
    return arr[dx][dy] != 0

direct = 0

arr[0][0] = 1

for i in range(2, n * m + 1):
    
    dx = x+dxs[direct]
    dy = y+dys[direct]

    if not isRange(dx,dy) or isFill(dx,dy):
        direct = (direct+1) % 4

    x = x+dxs[direct]
    y = y+dys[direct]

    arr[x][y] = i


for i in arr:
    for j in i:
        print(j,end=" ")
    print()