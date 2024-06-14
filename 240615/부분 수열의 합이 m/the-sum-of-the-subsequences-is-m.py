# import sys

# n, m = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))

# maxV = sys.maxsize

# dp= [maxV] * (m+1)


# dp[0] = 0


# for i in range(n):
#     for j in range(m,-1,-1):      #
#         if j>=arr[i] and dp[j-arr[i]] != maxV:
#             dp[j] = min(dp[j],dp[j-arr[i]] + 1)

# if dp[m] == maxV:
#     print(-1)
# else:
#     print(dp[m])

import sys

n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

maxV = sys.maxsize

dp = [maxV] * (m+1)

dp[0] = 0

for arr in arr:
    for j in range(m,-1,-1):
        if j>=arr and dp[j-arr] != maxV:
            dp[j] = min(dp[j - arr] + 1, dp[j])

if dp[m] == maxV:
    print(-1)
else:
    print(dp[m])