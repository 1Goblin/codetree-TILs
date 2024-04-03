import sys

n = int(input())
arr = list(map(int, input().split()))

m = sys.maxsize
cnt = 0
for i in arr:
    if i<=m:
        if m==i:
            cnt+=1
        else :
            cnt = 1
        m=i
        
print(m, cnt)