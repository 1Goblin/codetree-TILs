import sys

n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def ctr(i,j,k):
    
    return abs((arr[i][0] * arr[j][1] + arr[j][0] * arr[k][1] + arr[k][0] * arr[i][1]) -
    (arr[j][0] * arr[i][1] + arr[k][0] * arr[j][1] + arr[i][0] * arr[k][1]))

max_tr = -sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            area = ctr(i,j,k)
        max_tr = max(max_tr, area)

print(max_tr)