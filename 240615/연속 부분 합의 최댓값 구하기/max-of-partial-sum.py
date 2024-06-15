# import sys

# n = int(input())
# arr = list(map(int, input().split()))

# minV = -sys.maxsize

# dp = [minV] * (n+1)

# for i in range(1,n+1):
#     dp[i] = max(dp[i-1] + arr[i-1], arr[i-1])

# print(max(dp))

import sys

n = int(input())
arr = list(map(int, input().split()))

minV = -sys.maxsize

dp = [minV] * (n+1)

for i in range(1,n+1):
    dp[i] = max(dp[i-1] + arr[i-1], arr[i-1])


print(max(dp))