import sys

n = int(input())

arr = list(map(int, input().split()))

min_dis = sys.maxsize

for i in range(n):
    sumh = 0
    for j in range(n):
        sumh += arr[j] * abs(i-j)
    if min_dis > sumh:
        min_dis = sumh



print(min_dis)