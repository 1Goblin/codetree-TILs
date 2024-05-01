import sys

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


min_a = sys.maxsize
for i in range(n):
    narr = []
    for j in range(n):
        if i==j:
            continue
        narr.append(arr[j])
    narr.sort(key=lambda x : x[0])
    x = narr[n-2][0] - narr[0][0]
    narr.sort(key=lambda x : x[1])
    y = narr[n-2][1] - narr[0][1]
    area = x*y
    min_a = min(area, min_a)

print(min_a)