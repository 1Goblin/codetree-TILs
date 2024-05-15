n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0


for i in range(n):
    r = 0
    max_r = 0
    for j in range(n):
        if j!=0 and arr[i][j] == arr[i][j-1]:
            r+=1
        else:
            max_r = max(max_r,r)
            r = 0
    
    if (r+1)>=m:
        ans+=1

for i in range(n):
    c = 0
    max_c = 0
    for j in range(n):
        if j!=0 and arr[j][i] == arr[j-1][i]:
            c+=1
        else:
            max_c=max(max_c,c)
            c = 0
    if (c+1)>=m:
        ans+=1


print(ans)