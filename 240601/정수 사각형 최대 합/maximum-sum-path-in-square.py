n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dp[0][0] = arr[0][0]



for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue
        elif i==0:
            dp[i][j] = arr[i][j] + dp[i][j-1]
        elif j==0:
            dp[i][j] = arr[i][j] + dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + arr[i][j]

print(dp[n-1][n-1])