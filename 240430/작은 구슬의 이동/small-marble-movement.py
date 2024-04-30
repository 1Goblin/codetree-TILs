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


dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for i in range(t):

    nx = r + dx[d]
    ny = c + dy[d]

    if ran(nx,ny):
        r += dx[d]
        c += dy[d]
    else:
        d = 3-d



print(r+1, c+1)