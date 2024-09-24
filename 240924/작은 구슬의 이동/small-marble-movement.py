n, t = tuple(map(int, input().split(" ")))
r, c, d = input().split(" ")
r = int(r)
c = int(c)

ndx, ndy = [0,0,1,-1], [1,-1,0,0]

def inRange(x,y):
    return x>=1 and x<=n and y>=1 and y<=n


if d=="L":
    d= int(1)
elif d=="R":
    d= int(0)
elif d=="U":
    d= int(3)
elif d=="D":
    d= int(2)

for i in range(t):

    dx=r+ndx[d]
    dy=c+ndy[d]

    if not inRange(dx,dy):
        d= 1-d
        continue
    
    r+=ndx[d]
    c+=ndy[d]



print(r,c)