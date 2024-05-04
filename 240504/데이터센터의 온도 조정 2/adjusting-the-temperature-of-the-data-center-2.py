import sys

n, c, g, h = tuple(map(int, input().split()))
ans = -sys.maxsize

def cal_w(ta,tb,t):
    global c, g, h

    if t < ta:
        return c
    elif t >= ta and t<= tb:
        return g
    else:
        return h

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr.sort()

for i in range(arr[0][0],arr[n-1][1]):
    k = 0
    for j in range(n):
        k += cal_w(arr[j][0],arr[j][1], i)
    ans = max(ans,k)


print(ans)