import sys

n = int(input())

arr = [0] * 4

def swap(a,b):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c

max_c = -sys.maxsize

play = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
for i in range(1,4):
    arr[i] = 1
    cnt = 0
    for j in range(n):
        swap(play[j][0],play[j][1])
        if arr[play[j][2]] == 1:
            cnt+=1
    if max_c < cnt:
        ans = i
        max_c = cnt
    arr[i] = 0

print(max_c)