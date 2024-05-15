n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

r,c = tuple(map(int, input().split()))
r-=1
c-=1

power = arr[r][c]

for i in range(r-power+1,r+power):
    if i<0 or i>=n:
        continue
    for j in range(c-power+1,c+power):
        if j<0 or j>=n:
            continue
        if i==r or j==c:
            arr[i][j] = 0

for i in range(n):
    tem_r = n-1
    for j in range(n-1,-1,-1):
        if arr[j][i] !=0:
            temp[tem_r][i] = arr[j][i]
            tem_r-=1


for i in range(n):
    for j in range(n):
        print(temp[i][j],end=" ")
    print()