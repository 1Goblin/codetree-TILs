a = input()
b = input()
a = list(a)
b = list(b)
a_len = (len(a))
b_len = (len(b))

dp = [
    [0 for _ in range(b_len)]
    for _ in range(a_len)
]

def initialize():
    if a[0] == b[0]:
        dp[0][0] = 1

    for i in range(a_len):
        if a[i] == b[0]:
            for j in range(i,a_len):
                dp[j][0] = 1
            break
    
    for i in range(b_len):
        if b[i] == a[0]:
            for j in range(i,b_len):
                dp[0][j] = 1
            break
initialize()

for i in range(1, a_len):
    for j in range(1, b_len):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[a_len-1][b_len-1])