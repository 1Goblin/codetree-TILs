import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [sys.maxsize] * (m)

for i in arr:
    dp[i-1] = 1

for i in range(m):  #동전 금액 
    for j in range(i):  #비교할 동전 금액 
        if (i-j) in arr and dp[j] != sys.maxsize:
            dp[i] = min(dp[i], dp[j]+1)

if dp[m-1] == sys.maxsize:
    print(-1)
else:
    print(dp[m-1])