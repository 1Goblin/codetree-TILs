n = input()

x,y = 0,0

dx, dy = [0,1,0,-1], [1,0,-1,0]

direct = 0

for i in range(len(n)):
    if(n[i] == "L"):
        direct = (direct -1 ) % 4
    elif(n[i] == "R"):
        direct = (direct +1 ) % 4
    elif(n[i] == "F"):
        x+= dx[direct]
        y+= dy[direct]

print(x, y)