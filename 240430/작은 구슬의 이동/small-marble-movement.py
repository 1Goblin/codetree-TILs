da = {
    "U" : 0,
    "D" : 3,
    "R" : 1,
    "L" : 2
}

n, t = map(int, input().split())
r, c, d = input().split()

d = da[d]

r = int(r) -1
c = int(c) -1

def ran(x, y):
    return x>=0 and y>=0 and x<n and y<n



dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for i in range(t):

    if not ran(r,c):
        d = 3-d
    else: 
        arr[r][c] = 0
        r= r+dx[d]
        c= c+dy[d]
        arr[r][c] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            print(j, i)
            break