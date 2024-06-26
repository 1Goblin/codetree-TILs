# n = int(input())

# arr = list(map(int, input().split()))

# dp = [1]* n
# dp[0] = 1

# for i in range(1,n):
#     for j in range(i):
#         if arr[i]>arr[j] and dp[j] != 0:
#             dp[i] = max(dp[i], dp[j]+1)


# print(max(dp))


n = int(input())

arr = list(map(int, input().split()))

dp = [1] * (n)
dp[0] = 1



for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))