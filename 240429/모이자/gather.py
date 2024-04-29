import sys

n = int(input())

arr = list(map(int, input().split()))

min_dis = sys.maxsize
sumh = 0
for i in range(n):
    for j in range(n):
        sumh += arr[j] * abs(i-j)
    if min_dis > sumh:
        min_dis = sumh
    sumh = 0



print(min_dis)