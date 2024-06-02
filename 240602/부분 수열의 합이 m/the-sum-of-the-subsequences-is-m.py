import sys

n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))

maxV = sys.maxsize

dp = [maxV] * (m+1)

dp[0] = 0

for i in range(n):
    for j in range(m,-1,-1):
        if j>=A[i] and dp[j-A[i]] != maxV:
            dp[j] = min(dp[j],dp[j-A[i]]+1)


if dp[m] == maxV:
    print(-1)
else:
    print(dp[m])