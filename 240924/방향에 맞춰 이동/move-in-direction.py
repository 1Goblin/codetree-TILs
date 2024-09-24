n = int(input())

x, y = 0,0

dx, dy = [0,0,1,-1], [1,-1,0,0]


for _ in range(n):
    direct, dis = tuple(input().split())
    dis = int(dis)
    for i in range(dis):
        if(direct == "W"):
            x,y=x+dx[3], y+ dy[3]
        elif(direct == "S"):
            x,y=x+dx[1], y+ dy[1]
        elif(direct == "N"):
            x,y=x+dx[0], y+ dy[0]
        elif(direct == "E"):
            x,y=x+dx[2], y+ dy[2]

print(x, y)