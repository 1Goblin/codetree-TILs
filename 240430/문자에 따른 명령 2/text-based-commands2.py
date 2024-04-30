x, y = 0, 0
dx = [1,0,-1,0]
dy = [0,-1,0,1]
dir_m = list(input())
dir_n = 3

for i in range(len(dir_m)):
    if dir_m[i]=="L":
        dir_n = (dir_n - 1 + 4) % 4
    elif dir_m[i]=="R":
        dir_n = (dir_n +1) % 4
    elif dir_m[i]=="F":
        x += dx[dir_n]
        y += dy[dir_n]

print(x, y)