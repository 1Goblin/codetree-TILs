import sys
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = -sys.maxsize
for i in range(n-2):
    for j in range(n-2):
        cnt = 0
        for m in range(i,i+3):
            for n in range(i, i+3):
                if arr[m][n] == 1:
                    cnt+=1
        
        max_cnt = max(max_cnt, cnt)
print(max_cnt)