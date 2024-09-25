n = input()

dx, dy = [0,-1,0,1], [1,0,-1,0]

x, y = 0, 0

direct = 0
ans = -1
start = 0

for i in range(len(n)):

    if n[i] == "L":
        direct = (direct + 1) % 4
    elif n[i] == "R":
        direct = (direct - 1) %4 
    elif n[i] == "F":
        x += dx[direct]
        y += dy[direct]
        start = 1

    if x==0 and y==0 and start == 1:
        ans = i+1
        break

print(ans)