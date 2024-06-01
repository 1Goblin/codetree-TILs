n = int(input())
arr = list(map(int, input().split()))

ans = []

dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n):
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        dp[i] = max(dp[j]+1,dp[i])

print(max(dp))