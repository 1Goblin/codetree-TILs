n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * m

for i in arr:
    dp[i-1] = 1

for i in range(m):
    for j in range(i):
        if (i-j) in arr and dp[j] != 0:
            if dp[i] == 0:
                dp[i] = dp[j] + 1
            else:
                dp[i] = min(dp[i], dp[j] + 1)


print(dp[m-1])