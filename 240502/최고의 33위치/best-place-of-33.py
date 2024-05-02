import sys

max_s = -sys.maxsize

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)    
]

def sa(r,c):
    s = 0
    for i in range(r, r+3):
        for j in range(c, c+3):
            s += arr[i][j]
    return s

for i in range(n-2):
    for j in range(n-2):
        max_s = max(sa(i,j), max_s)

print(max_s)