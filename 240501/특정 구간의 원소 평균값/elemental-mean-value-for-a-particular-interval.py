n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i, n):
        s,a = 0,0
        for k in range(i, j+1):
            s+= arr[k]
            a +=1
        mean = s/a
        for l in range(i, j+1):
            if mean==arr[l]:
                cnt+=1
                break
            
print(cnt)