import sys

n, m =tuple(map(int, input().split()))

dresses = [
    list(map(int, input().split()))
    for _ in range(n)
]

minV = -sys.maxsize

# n개의 옷
# m일 동안 옷을 적절하게 입기
# s = 옷을 입기 시작할 수 있는날짜, 0
# e = 해당옷을 입 을 수 있는 마지막날짜, 1
# v = 그 옷의 화려함, 2

dp = [
    [minV for _ in range(n)]
    for _ in range(m)
]

def initialize():

    for i in range(n):
        if dresses[i][0] == 1:
            dp[0][i] = 0

initialize()


for i in range(1,m):      #일수 
    for j in range(n):  #전날 최대 값 
        for k in range(n): #당일 무슨옷 입을지
            if dresses[k][0] <= (i+1) and  (i+1) <= dresses[k][1] and dp[i-1][j] != minV:
                at = abs(dresses[j][2] - dresses[k][2])
                dp[i][k] = max(dp[i][k],at + dp[i-1][j])

print(max(dp[m-1]))