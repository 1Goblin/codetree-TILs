n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i, n):
        s,n = 0,0
        for k in range(i, j+1):
            s+= arr[k]
            n +=1
        s = s/n
        for l in range(i, j+1):
            if s==arr[l]:
                cnt+=1


print(cnt)