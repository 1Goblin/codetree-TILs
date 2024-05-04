import sys

def cal_t(arr):
    ar = sorted(arr)
    t = ar[0][1] - ar[0][0]

    for i in range(1,len(ar)):
        if ar[i-1][1]>ar[i][0]:
            t += ar[i][1] -ar[i-1][1]
        else:
            t += ar[i][1] - ar[i][0]
        
    return t

[[46, 138], [186, 288], [274, 380], [373, 451]]
[[46, 138], [134, 203], [274, 380], [373, 451]]
[[46, 138], [134, 203], [186, 288], [373, 451]]
[[134, 203], [186, 288], [274, 380], [373, 451]]
[[46, 138], [134, 203], [186, 288], [274, 380]]

n = int(input())
max_t = -sys.maxsize

all_p = [
    list(map(int, input().split()))
    for _ in range(n)
]


for i in range(n):
    ef_p = []
    for k in range(n):
        if i==k:
            continue
        ef_p.append(all_p[k])
    
    max_t = max(max_t,cal_t(ef_p))

print(max_t)