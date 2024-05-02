import sys

n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def ctr(ar : list):
    
    return abs((ar[0][0] * ar[1][1] + ar[1][0] * ar[2][1] + ar[2][0] * ar[0][1]) -
    (ar[1][0] * ar[0][1] + ar[2][0] * ar[1][1] + ar[0][0] * ar[2][1]))

max_tr = -sys.maxsize

for i in range(n):
    tr = []
    for j in range(n):
        if i==j:
            continue
        tr.append(arr[j])
    area=ctr(tr)
    max_tr = max(max_tr, area)

        
print(max_tr)