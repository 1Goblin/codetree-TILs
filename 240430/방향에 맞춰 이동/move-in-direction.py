n = int(input())
x, y = 0, 0
dx, dy = [1,0,-1,0], [0,-1,0,1]


for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == "W":
        a = 2
    elif a == "S":
        a = 1
    elif a == "N":
        a = 3
    elif a == "E":
        a = 0
    
    for j in range(b):
        x, y = x + dx[a], y + dy[a]

print(x, y)