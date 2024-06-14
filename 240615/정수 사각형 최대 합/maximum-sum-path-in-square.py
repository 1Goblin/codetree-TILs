# n = int(input())

# arr = [
#     list(map(int, input().split())) + [0,0,0]
#     for _ in range(n)
# ]

# arr.append([0] * (n*3))
# arr.append([0] * (n*3))
# arr.append([0] * (n*3))


# dp = [
#     [0 for _ in range(n+3)]
#     for _ in range(n+3)
# ]

# dp[0][0] = arr[0][0]

# for i in range(n):
#     for j in range(n):
#         dp[i+1][j] = max(dp[i+1][j], arr[i+1][j] + dp[i][j])
#         dp[i][j+1] = max(dp[i][j+1], arr[i+1][j] + dp[i][j])

# print(dp[n-1][n-1])



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

def can_go(x,y):
    return x>0 and y>0 and x<n and y<n 

for i in range(1,n):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1,n):
    for j in range(1,n):
        if can_go(i,j):
            dp[i][j] = max(dp[i-1][j]+arr[i][j], dp[i][j-1]+arr[i][j])


print(dp[-1][-1])