import sys
n = int(input())

arr = list(map(int, input().split()))

min_ans = sys.maxsize

for i in range(n):
    ans = 0
    for j in range(n):

        if j==i:
            continue
        ans += abs(i-j)*arr[j]
    
    min_ans = min(min_ans, ans)

print(min_ans)