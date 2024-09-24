n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0

ndx, ndy = [0,0,1,-1], [1,-1,0,0]

def inRange(x,y):
    if (x<0 or y<0 or x>=n or y>=n):
        return True
    return False

for x in range(n):
    for y in range(n):
        count = 0
        for dx, dy in zip(ndx, ndy):
            if((inRange(x+dx, y+dy))):
                continue

            if(arr[x+dx][y+dy] == 1):
                count+=1
        if(count>=3):
            ans +=1
print(ans)