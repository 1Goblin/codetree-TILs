n = input()

x,y = 0,0

dx, dy = [0,0,1,-1], [1,-1,0,0]

direct = 0

for i in range(len(n)):
    if(n[i] == "L"):
        direct = 3
    elif(n[i] == "R"):
        direct = 2
    elif(n[i] == "F"):
        x+= dx[direct]
        y+= dy[direct]

print(x, y)