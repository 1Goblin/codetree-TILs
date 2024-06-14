# import sys

# n, m = tuple(map(int, input().split()))

# coin = list(map(int, input().split()))

# maxV = sys.maxsize

# dp = [maxV] * (m+1)

# dp[0] = 0


# for i in range(1,m+1):
#     for j in range(n):
#         if i>=coin[j] and dp[i-coin[j]] != maxV:
#             dp[i] = min(dp[i], dp[i-coin[j]] + 1)

# if dp[m] == maxV:
#     print(-1)
# else:
#     print(dp[m])


import sys

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

maxV = sys.maxsize

dp = [maxV] * (m+1)

for i in arr:
    dp[i] = 1

dp[0] = 0

for i in range(1,m+1):
    for coin in arr:
        if i>=coin and dp[i-coin] != maxV:
            dp[i] = min(dp[i-coin] + 1, dp[i])


if dp[m] == maxV:
    print(-1)
else:
    print(dp[m])