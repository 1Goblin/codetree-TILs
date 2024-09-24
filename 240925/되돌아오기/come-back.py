N = int(input())

r,c = 0,0
ans = -1
count = 0

dx, dy = [0,0,1,-1], [1,-1,0,0]

direct = {
    "N":3,
    "E":0,
    "W":1,
    "S":2
}

def move(d):
    global r, c, count
    r+=dx[direct[d]]
    c+=dy[direct[d]]
    count+=1
    

for i in range(N):
    d, m = input().split()
    m = int(m)

    

    for j in range(m):
        move(d)
        if (r==0 and c==0):
            ans = count
    
    if ans != -1:
        break


print(ans)