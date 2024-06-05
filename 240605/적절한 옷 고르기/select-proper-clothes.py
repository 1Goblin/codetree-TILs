import sys

n, m =tuple(map(int, input().split()))

dresses = [
    list(map(int, input().split()))
    for _ in range(n)
]

minV = 0

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
        if dresses[i][1] <= (i+1) and  (i+1) <= dresses[i][2]:
            dp[0][i] = dresses[i][2]

initialize()


for i in range(m):      #일수 
    for j in range(n):  #전날 최대 값 
        for k in range(n): #당일 무슨옷 입을지
            if dresses[k][0] <= (k+1) and  (k+1) <= dresses[k][1]:
                dp[i][k] = max(dp[i][k],abs(dp[i-1][j] - dresses[k][2]))

print(max(dp[m-1]))