c = input().split()
n = int(c[0])
m = int(c[1])
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i==m:
        cnt+=1
print(cnt)